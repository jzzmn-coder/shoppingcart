"""
Module 2: Automatic Billing System
Calculates live total bill, itemized discounts, taxes, and final receipt without manual scanning.
"""

import pandas as pd

class SmartBillingSystem:
    def __init__(self, products_csv="dataset/products.csv"):
        self.products_df = pd.read_csv(products_csv)
        self.cart = []
        self.tax_rate = 0.05 # 5% GST

    def add_item(self, product_name):
        match = self.products_df[self.products_df['product_name'].str.lower() == product_name.lower()]
        if match.empty:
            return {"error": "Product not found"}
        
        item = match.iloc[0].to_dict()
        self.cart.append(item)
        return self.calculate_bill()

    def remove_item(self, product_id):
        self.cart = [item for item in self.cart if item['product_id'] != product_id]
        return self.calculate_bill()

    def calculate_bill(self):
        subtotal = sum([item['price'] for item in self.cart])
        discounts = sum([item['price'] * (item['discount_percent'] / 100.0) for item in self.cart])
        taxable_amount = subtotal - discounts
        tax = taxable_amount * self.tax_rate
        final_total = taxable_amount + tax

        return {
            "item_count": len(self.cart),
            "items": self.cart,
            "subtotal": round(subtotal, 2),
            "discounts": round(discounts, 2),
            "tax": round(tax, 2),
            "final_total": round(final_total, 2)
        }

if __name__ == "__main__":
    billing = SmartBillingSystem()
    billing.add_item("Organic Fresh Milk 1L")
    billing.add_item("Whole Wheat Bread 400g")
    print(billing.calculate_bill())
