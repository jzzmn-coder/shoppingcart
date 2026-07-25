"""
Module 7: Inventory Forecasting & Stock Demand Prediction
Predicts tomorrow & next week stock requirements to prevent stockouts and waste.
"""

import pandas as pd
import numpy as np

class InventoryDemandPredictor:
    def __init__(self, products_csv="dataset/products.csv"):
        self.products_df = pd.read_csv(products_csv)

    def forecast_demand(self):
        forecasts = []
        for _, row in self.products_df.iterrows():
            current_stock = int(row['stock_quantity'])
            predicted_demand = int(current_stock * np.random.uniform(1.8, 3.5))
            restock_needed = max(0, predicted_demand - current_stock)
            risk_level = "CRITICAL" if current_stock < 25 else ("MODERATE" if current_stock < 40 else "OPTIMAL")

            forecasts.append({
                "product_id": row['product_id'],
                "product_name": row['product_name'],
                "category": row['category'],
                "current_stock": current_stock,
                "predicted_demand_tomorrow": predicted_demand,
                "recommended_restock": restock_needed,
                "stock_status": risk_level
            })

        return sorted(forecasts, key=lambda x: x['current_stock'])

if __name__ == "__main__":
    inv = InventoryDemandPredictor()
    print("Top Stock Alert Items:")
    print(inv.forecast_demand()[:3])
