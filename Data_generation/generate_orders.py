import csv
import uuid
import random
from datetime import datetime, timedelta

PRODUCTS = [
    ("P101", "Laptop", 75000),
    ("P102", "Phone", 40000),
    ("P103", "Tablet", 30000),
    ("P104", "Monitor", 15000),
    ("P105", "Keyboard", 2000)
]

WAREHOUSES = ["WH_BLR", "WH_DEL", "WH_MUM", "WH_CHE"]
STATUSES = ["CREATED", "PACKED", "SHIPPED"]

OUTPUT_FILE = "orders.csv"
TOTAL_RECORDS = 5000

start_time = datetime.now() - timedelta(days=1)

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "order_id",
        "product_id",
        "product_name",
        "quantity",
        "unit_price",
        "warehouse_id",
        "order_status",
        "order_timestamp"
    ])

    for _ in range(TOTAL_RECORDS):
        product = random.choice(PRODUCTS)
        quantity = random.randint(1, 5)

        writer.writerow([
            str(uuid.uuid4()),
            product[0],
            product[1],
            quantity,
            product[2],
            random.choice(WAREHOUSES),
            random.choice(STATUSES),
            (start_time + timedelta(seconds=random.randint(1, 86400))).isoformat()
        ])

print("✅ orders.csv generated successfully")
