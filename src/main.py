def display_product_info(data):
    print("📦 Product Details 📦")
    print(f"Item Name: {data['title']}")
    
    print(f"Price: ${data['price']:.2f}") 
    print(f"Categories: {', '.join(data['categories'])}")
    print(f"In Stock: {'Yes' if data['in_stock'] else 'No (Out of Stock)'}")
    print("-----------------------")

product = {
    "title": "Bathroom Tissue",
    "price": 3.20, 
    "categories": ["Household"],
    "in_stock": True
}

if __name__ == "__main__":
    display_product_info(product)