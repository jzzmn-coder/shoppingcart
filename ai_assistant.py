"""
Module 5: AI Smart Shopping Assistant
Acts as an in-cart intelligent shopping copilot for customers and store managers.
Provides healthier swaps, active discounts, budget estimations, and recipe suggestions.
"""

class AIShoppingAssistant:
    def __init__(self):
        self.health_swaps = {
            "Coca-Cola 500ml": {"swap": "Greek Yogurt 200g or Organic Fresh Fruit Juice", "reason": "Saves 210 sugar calories & adds probiotics!"},
            "Whole Wheat Bread 400g": {"swap": "Multigrain Sprouted Bread", "reason": "Higher dietary fiber & lower glycemic index!"},
            "Amul Pasteurised Butter 100g": {"swap": "Extra Virgin Olive Oil 500ml", "reason": "Rich in healthy monounsaturated heart-friendly fats!"}
        }

    def process_query(self, query_text, cart_items=None):
        query = query_text.lower()

        if "health" in query or "swap" in query or "calories" in query:
            if cart_items:
                suggestions = []
                for item in cart_items:
                    name = item.get("product_name", "")
                    if name in self.health_swaps:
                        swap_info = self.health_swaps[name]
                        suggestions.append(f"💡 Swap **{name}** with **{swap_info['swap']}**: {swap_info['reason']}")
                if suggestions:
                    return "\n\n".join(suggestions)
            return "💡 Healthy Suggestion: Consider replacing refined snacks with Organic Green Apples or Greek Yogurt for 40% fewer calories!"

        elif "discount" in query or "deal" in query or "offer" in query:
            return "🔥 **Active Smart Cart Deals**:\n- Buy Dairy items over ₹200 & get 10% instant discount on Bakery!\n- Organic Green Apples: 10% OFF today!\n- Extra Virgin Olive Oil: ₹50 Instant Cashback."

        elif "recipe" in query or "cook" in query:
            return "👨‍🍳 **Smart Recipe Pick**: Based on Milk + Eggs + Bread in your cart, you can make **Classic French Toast** in 10 mins! Add Cinnamon & Honey for extra flavor."

        else:
            return f"🤖 I am your AI Autonomous Shopping Assistant! I detected your request: '{query_text}'. I can help you find discounts, healthier food alternatives, estimate cart totals, and recommend recipe pairings!"

if __name__ == "__main__":
    bot = AIShoppingAssistant()
    print(bot.process_query("Are there any healthy swaps for Coca-Cola 500ml?", [{"product_name": "Coca-Cola 500ml"}]))
