orders = [
    {
        "order_id": "ORD001",
        "product": "Laptop",
        "quantity": 1,
        "total_amount": 1200.00,
        "order_date": "2025-06-01",
        "order_status": "Shipped"
    },
    {
        "order_id": "ORD002",
        "product": "Smartphone",
        "quantity": 2,
        "total_amount": 1600.00,
        "order_date": "2025-06-03",
        "order_status": "Processing"
    },
    {
        "order_id": "ORD003",
        "product": "Headphones",
        "quantity": 3,
        "total_amount": 300.00,
        "order_date": "2025-06-05",
        "order_status": "Delivered"
    },
    {
        "order_id": "ORD004",
        "product": "Monitor",
        "quantity": 1,
        "total_amount": 250.00,
        "order_date": "2025-06-07",
        "order_status": "Pending"
    },
    {
        "order_id": "ORD005",
        "product": "Keyboard",
        "quantity": 4,
        "total_amount": 200.00,
        "order_date": "2025-06-09",
        "order_status": "Pending"
    }
]
#Find the Total Number of ordered
total_order = sum(order['quantity'] for order in orders)
print("Total No of orders:",total_order)
#Add a new field called Product_category where items are grouped
#Devices :'laptop','Smartphones','Tablets'
#Accessories:'Headphones','Monitors','Keyboards','Mouse'
def assign_category(product_name):
    devices = {'laptop','Smartphones','Tablets'}
    Accessories= {'Headphones', 'Monitors', 'Keyboards', 'Mouse'}
    product_lower = product_name.lower()
    if product_name in devices:
        return "Devices"
    elif product_lower in Accessories:
        return "Accessories"
    else:
        return "Others"


for order in orders:
    order['product_cate'] = assign_category(order["product"])
