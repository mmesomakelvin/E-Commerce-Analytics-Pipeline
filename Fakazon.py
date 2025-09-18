import csv
import os
import random
from datetime import datetime, timedelta
from faker import Faker

# Initialize once
f = Faker()
Record_count = 50000
Product_count = 1000
Order_count = 75000  # More orders than customers (some customers order multiple times)

nigerian_cities = [
    'Lagos, Nigeria', 'Abuja, Nigeria', 'Kano, Nigeria',
    'Ibadan, Nigeria', 'Port Harcourt, Nigeria', 'Kaduna, Nigeria'
]

product_categories = [
    'Electronics', 'Clothing', 'Books', 'Home & Garden', 'Sports',
    'Beauty', 'Toys', 'Automotive', 'Health', 'Food'
]

product_names = [
    'Wireless Headphones', 'T-Shirt', 'Novel Book', 'Coffee Mug', 'Running Shoes',
    'Face Cream', 'Action Figure', 'Car Charger', 'Vitamin C', 'Snack Box',
    'Smartphone', 'Jeans', 'Cookbook', 'Plant Pot', 'Basketball',
    'Lipstick', 'Puzzle Game', 'Phone Holder', 'Protein Powder', 'Tea Bags',
    'Laptop', 'Sweater', 'Magazine', 'Lamp', 'Yoga Mat'
]

payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Mobile Money']
shipping_statuses = ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled']

def create_customers_csv():
    print(f"Creating {Record_count} customers...")
    os.makedirs('./files', exist_ok=True)
    
    with open('./files/customers.csv', 'w', newline='') as csvfile:
        fieldnames = ['customer_id', 'name', 'email', 'signup_date', 'location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(Record_count):
            start_date = datetime(2022, 1, 1)
            end_date = datetime(2024, 9, 1)
            days_between = (end_date - start_date).days
            random_days = random.randint(0, days_between)
            signup_date = start_date + timedelta(days=random_days)
            
            writer.writerow({
                'customer_id': i + 1,
                'name': f.name(),
                'email': f.unique.email(),
                'signup_date': signup_date.strftime('%Y-%m-%d'),
                'location': random.choice(nigerian_cities)
            })
    
    print(f"✅ Created {Record_count} customers successfully!")

def create_products_csv():
    print(f"Creating {Product_count} products...")
    
    with open('./files/products.csv', 'w', newline='') as csvfile:
        fieldnames = ['product_id', 'name', 'category', 'price', 'stock_quantity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(Product_count):
            price = round(random.uniform(5.0, 500.0), 2)
            stock = random.randint(0, 1000)
            
            writer.writerow({
                'product_id': i + 1,
                'name': f"{random.choice(product_names)} {i+1}",
                'category': random.choice(product_categories),
                'price': price,
                'stock_quantity': stock
            })
    
    print(f"✅ Created {Product_count} products successfully!")

def create_orders_csv():
    print(f"Creating {Order_count} orders...")
    
    with open('./files/orders.csv', 'w', newline='') as csvfile:
        fieldnames = ['order_id', 'customer_id', 'product_id', 'quantity', 'price', 'order_date', 'shipping_status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(Order_count):
            # Random customer (1 to Record_count)
            customer_id = random.randint(1, Record_count)
            
            # Random product (1 to Product_count)  
            product_id = random.randint(1, Product_count)
            
            # Random quantity (1-5 items per order)
            quantity = random.randint(1, 5)
            
            # Random price (simulate discounts/variations)
            base_price = round(random.uniform(5.0, 500.0), 2)
            total_price = round(base_price * quantity, 2)
            
            # Random order date (customers can only order after they sign up)
            start_date = datetime(2022, 6, 1)  # Orders start after some customers signed up
            end_date = datetime(2024, 9, 15)
            days_between = (end_date - start_date).days
            random_days = random.randint(0, days_between)
            order_date = start_date + timedelta(days=random_days)
            
            writer.writerow({
                'order_id': i + 1,
                'customer_id': customer_id,
                'product_id': product_id,
                'quantity': quantity,
                'price': total_price,
                'order_date': order_date.strftime('%Y-%m-%d'),
                'shipping_status': random.choice(shipping_statuses)
            })
    
    print(f"✅ Created {Order_count} orders successfully!")

def create_payments_csv():
    print(f"Creating {Order_count} payments...")
    
    with open('./files/payments.csv', 'w', newline='') as csvfile:
        fieldnames = ['payment_id', 'order_id', 'payment_method', 'payment_date', 'amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(Order_count):
            # Each order has exactly one payment
            order_id = i + 1
            
            # Payment usually happens same day or 1-2 days after order
            days_delay = random.randint(0, 2)
            
            # Generate payment date (we'll use a base date and add the delay)
            start_date = datetime(2022, 6, 1)
            end_date = datetime(2024, 9, 15)
            days_between = (end_date - start_date).days
            random_days = random.randint(0, days_between)
            payment_date = start_date + timedelta(days=random_days + days_delay)
            
            # Payment amount (same as order price with small variations for fees/taxes)
            base_amount = round(random.uniform(5.0, 500.0) * random.randint(1, 5), 2)
            amount = round(base_amount * random.uniform(1.0, 1.1), 2)  # Add 0-10% for taxes/fees
            
            writer.writerow({
                'payment_id': i + 1,
                'order_id': order_id,
                'payment_method': random.choice(payment_methods),
                'payment_date': payment_date.strftime('%Y-%m-%d'),
                'amount': amount
            })
    
    print(f"✅ Created {Order_count} payments successfully!")

def create_all_tables():
    print("🚀 Starting E-commerce Data Pipeline...")
    print("=" * 50)
    
    create_customers_csv()
    create_products_csv() 
    create_orders_csv()
    create_payments_csv()
    
    print("=" * 50)
    print("🎉 All tables created successfully!")
    print("\nFiles created:")
    print("📁 ./files/customers.csv")
    print("📁 ./files/products.csv") 
    print("📁 ./files/orders.csv")
    print("📁 ./files/payments.csv")

if __name__ == "__main__":
    create_all_tables()