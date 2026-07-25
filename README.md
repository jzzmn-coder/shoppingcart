 🛒 AI Autonomous Shopping Cart & Smart Billing System

An end-to-end intelligent retail automation platform that combines **Computer Vision**, **Deep Learning (RNN/LSTM)**, **Machine Learning Recommendation Engines**, and **Real-Time Analytics Dashboards** to revolutionize modern in-store shopping and inventory management.

---

 🚀 Key Features

* **📷 Computer Vision Billing (CNN Product Recognition)**
  * Automatic real-time product classification via camera feed without scanning physical barcodes.
  * Instant retrieval of product details, category, unit price, and confidence score.

* **🛒 Automated Cart & Dynamic Billing**
  * Instant live cart updates, automatic promotional discount application, tax calculation, and real-time total updates.

* **🎯 ML Recommendation Engine (KNN & Apriori)**
  * Uses K-Nearest Neighbors and Association Rule Mining to suggest relevant complementary products while shopping.

* **📈 Customer Purchase Sequence Prediction (RNN/LSTM)**
  * Recurrent Neural Network models analyzing historical customer purchase cycles to predict next-week replenishment needs.

* **🤖 AI In-Cart Assistant**
  * Interactive natural language shopping assistant guiding users with healthy alternatives, budget tracking, active promotions, and recipe ideas.

* **📊 Store Analytics & Executive Dashboard**
  * Comprehensive visual dashboard presenting real-time store metrics, peak sales hours, revenue trends, top-performing items, and customer segmentation (RFM analysis).

* **📦 Inventory Demand Forecasting**
  * Machine learning demand prediction algorithm forecasting daily inventory restocking requirements to prevent stockouts.

---

 🛠️ Tech Stack & Architecture

* **Backend & API:** Python, Flask, Flask-CORS
* **Machine Learning & AI:** TensorFlow / Keras (CNN & LSTM), Scikit-Learn (KNN), Pandas, NumPy
* **Frontend:** HTML5, Modern CSS3, JavaScript, Vite, Chart.js
* **Dataset & Storage:** CSV / Data Pipelines

---

 📁 Repository Structure

```text
├── dataset/             # Product catalog, customer history, and sales dataset
├── models/              # Pre-trained CNN, LSTM, and ML model artifacts
├── modules/             # Core Python modules (Vision, Billing, Recommender, Inventory, etc.)
├── app.py               # Flask REST API Server
├── customer.html        # Customer Portal UI
├── admin.html           # Store Admin & Analytics Dashboard
├── requirements.txt     # Python Dependencies
└── package.json         # Node.js / Vite Configuration
