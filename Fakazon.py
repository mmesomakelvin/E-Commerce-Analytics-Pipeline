import csv
import os
import random
from datetime import datetime, timedelta
from faker import Faker

f = Faker()
Record_count = 50000  

nigerian_cities = [
    'Lagos, Nigeria', 'Abuja, Nigeria', 'Kano, Nigeria',
    'Ibadan, Nigeria', 'Port Harcourt, Nigeria'
]

def create_csv_file():
    print(f"Record_count = {Record_count}")
    print(f"Type = {type(Record_count)}")
    
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
    
    print(f"Created {Record_count} customer records successfully!")

if __name__ == "__main__":
    create_csv_file()




import csv
import os
import random
from datetime import datetime, timedelta
from faker import Faker

f = Faker()
Record_count = 50000  

nigerian_cities = [
    'Lagos, Nigeria', 'Abuja, Nigeria', 'Kano, Nigeria',
    'Ibadan, Nigeria', 'Port Harcourt, Nigeria'
]

# Product categories and names
product_categories = [
    'Electronics', 'Clothing', 'Books', 'Home & Garden', 'Sports',
    'Beauty', 'Toys', 'Automotive', 'Health', 'Food'
]

product_names = [
    'Wireless Headphones', 'T-Shirt', 'Novel Book', 'Coffee Mug', 'Running Shoes',
    'Face Cream', 'Action Figure', 'Car Charger', 'Vitamin C', 'Snack Box',
    'Smartphone', 'Jeans', 'Cookbook', 'Plant Pot', 'Basketball',
    'Lipstick', 'Puzzle Game', 'Phone Holder', 'Protein Powder', 'Tea Bags',
    'Laptop', 'Sweater', 'Magazine', 'Lamp', 'Yoga Mat',
    'Shampoo', 'Board Game', 'Tire Gauge', 'First Aid Kit', 'Chocolate Bar'
]

def create_customers_csv():
    print(f"Creating customers... Record_count = {Record_count}")
    
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
    
    print(f"Created {Record_count} customer records successfully!")

def create_products_csv():
    print(f"Creating products...")
    
    # Use fewer products than customers (more realistic)
    product_count = 1000
    
    with open('./files/products.csv', 'w', newline='') as csvfile:
        fieldnames = ['product_id', 'name', 'category', 'price', 'stock_quantity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(product_count):
            # Generate random price between $5 and $500
            price = round(random.uniform(5.0, 500.0), 2)
            
            # Generate stock quantity between 0 and 1000
            stock = random.randint(0, 1000)
            
            writer.writerow({
                'product_id': i + 1,
                'name': f"{random.choice(product_names)} {i+1}",
                'category': random.choice(product_categories),
                'price': price,
                'stock_quantity': stock
            })
    
    print(f"Created {product_count} product records successfully!")

def create_all_tables():
    print("Starting to create all CSV files...")
    create_customers_csv()
    create_products_csv()
    print("All tables created successfully!")

if __name__ == "__main__":
    create_all_tables()