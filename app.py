"""
Main Application Server - AI Autonomous Shopping Cart & Smart Billing System
Integrates CNN product vision, ML recommendations, LSTM purchase sequence predictions, 
inventory demand forecasting, and store analytics dashboards.
"""

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import os

from modules.product_detection import ProductCNNClassifier
from modules.billing import SmartBillingSystem
from modules.recommendation import RecommendationEngine
from modules.purchase_prediction import PurchaseSequencePredictor
from modules.inventory import InventoryDemandPredictor
from modules.dashboard import StoreAnalyticsDashboard
from modules.ai_assistant import AIShoppingAssistant

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Initialize Modules
cnn = ProductCNNClassifier()
billing = SmartBillingSystem()
recommender = RecommendationEngine()
sequence_predictor = PurchaseSequencePredictor()
inventory_predictor = InventoryDemandPredictor()
analytics = StoreAnalyticsDashboard()
assistant = AIShoppingAssistant()

@app.route('/')
@app.route('/customer')
def customer_portal():
    return send_from_directory('.', 'customer.html')

@app.route('/admin')
def admin_portal():
    return send_from_directory('.', 'admin.html')

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "active", "system": "AI Autonomous Shopping Cart API", "version": "1.0.0"})

@app.route('/api/detect-product', methods=['POST'])
def detect_product():
    data = request.json or {}
    product_name = data.get('product_name', None)
    result = cnn.predict_product(product_name)
    return jsonify(result)

@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    data = request.json or {}
    product_name = data.get('product_name', 'Organic Fresh Milk 1L')
    cart_summary = billing.add_item(product_name)
    
    # Get dynamic recommendations
    current_items = [item['product_name'] for item in cart_summary.get('items', [])]
    recommendations = recommender.get_recommendations(current_items)

    return jsonify({
        "cart": cart_summary,
        "recommendations": recommendations
    })

@app.route('/api/predict-sequence', methods=['GET'])
def predict_sequence():
    customer_id = request.args.get('customer_id', 'C101')
    return jsonify(sequence_predictor.predict_next_week(customer_id))

@app.route('/api/inventory-forecast', methods=['GET'])
def inventory_forecast():
    return jsonify(inventory_predictor.forecast_demand())

@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    return jsonify({
        "summary": analytics.get_summary_metrics(),
        "charts": analytics.get_chart_data()
    })

@app.route('/api/assistant', methods=['POST'])
def assistant_chat():
    data = request.json or {}
    query = data.get('query', '')
    cart = data.get('cart', [])
    response_text = assistant.process_query(query, cart)
    return jsonify({"response": response_text})

if __name__ == '__main__':
    print("Starting AI Autonomous Shopping Cart & Billing API Server on port 5000...")
    app.run(host='0.0.0.0', port=5000, debug=True)
