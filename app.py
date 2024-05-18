from flask import Flask, request, jsonify
import random

# Replace these with actual product details (descriptions removed)
products = {
    "Lovely Lilly": {"weight": 100, "price": 3.99},
    "Citrus Splash": {"weight": 120, "price": 4.49},
    "Minty Mist": {"weight": 80, "price": 2.99},
    "Lavender Dreams": {"weight": 150, "price": 5.99},
    "Lemongrass Zest": {"weight": 110, "price": 4.29},
    "Aloe Vera Soothe": {"weight": 100, "price": 3.99},
    "Sandalwood Serenity": {"weight": 120, "price": 4.49},
    "Tea Tree Tingle": {"weight": 90, "price": 3.79},
    "Cocoa Butter Bliss": {"weight": 130, "price": 4.99},
    "Eucalyptus Mint Magic": {"weight": 100, "price": 3.99},
    "Patchouli Passion": {"weight": 120, "price": 4.49},
    "Shea Butter Silk": {"weight": 80, "price": 2.99},
    "Rosemary Revive": {"weight": 110, "price": 4.29},
    "Oatmeal Honey Glow": {"weight": 100, "price": 3.99},
    "Gold Dust Luxury": {"weight": 150, "price": 35.99},
    "Diamond Elegance": {"weight": 120, "price": 45.99},
    "Platinum Silk": {"weight": 100, "price": 32.99},
    "Truffle Delight": {"weight": 120, "price": 38.99},
    "Royal Jasmine": {"weight": 150, "price": 34.99},
    "Silk Blossom": {"weight": 120, "price": 19.99},
    "Exotic Coconut": {"weight": 100, "price": 16.99},
    "Mandarin Sunrise": {"weight": 110, "price": 22.99},
    "Bamboo Charcoal Detox": {"weight": 120, "price": 24.99},
    "Herbal Garden": {"weight": 90, "price": 14.99},
}

def generate_sales_data(num_records):
    data = []
    for _ in range(num_records):
        product_name = random.choice(list(products.keys()))
        quantity = random.randint(1, 3)
        discount = round(random.uniform(0, 0.99) * products[product_name]["price"], 2)
        final_price = products[product_name]["price"] * quantity - discount
        profit_margin = 0.1 if final_price < 10 else (0.2 if final_price < 20 else 0.25)
        profit = round(final_price * profit_margin, 2)
        data.append({
            "Date": f"{random.randint(2024, 2024)}{random.randint(10, 12)}{random.randint(1, 29)}",
            "Order-ID": f"ORD-{random.randint(100000, 999999)}",
            "Product Name": product_name,
            "Quantity": quantity,
            "Rate (GBP)": products[product_name]["price"],
            "Discount (GBP)": discount,
            "Final Price (GBP)": final_price,
            "Profit Margin": f"{profit_margin:.0%}",
            "Profit (GBP)": profit,
        })
    return data

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    num_records = 1000
    data = generate_sales_data(num_records)

    # Convert data to CSV format
    csv_data = ""
    headers = [key for key in data[0]]  # Extract headers from first record
    csv_data += ",".join(headers) + "\n"  # Add header row
    for row in data:
        csv_data += ",".join([str(value) for value in row.values()]) + "\n"

    # You can now use this CSV data for further processing
    # (e.g., print it, write it to a file, or return it as a response)

    # Example: Print the generated CSV data
    print(csv_data)

    # Example: Return the CSV data as a Flask response
    # return jsonify(data)  # This would return JSON instead of CSV

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode
