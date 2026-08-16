"""
Exercise: Nested order summary
Student: Sabita Rajbanshi 
Day: 2

"""
# dictionary of 3 different orders
orders = {
    "ORD-001": {"customer": "Anisha", "amount": 2500, "status": "Completed"},
    "ORD-002": {"customer": "Ravi", "amount": 1800, "status": "Pending"},
    "ORD-003": {"customer": "Maya", "amount": 3200, "status": "Completed"},
}

# 1. print every order ID and customer
print("Order ID and Customer:")
for order_id, order in orders.items():
    print(order_id, "-", order["customer"])

# 2. print only completed orders
print("\nCompleted Orders:")
for order_id, order in orders.items():
    if order["status"] == "Completed":
        print(order_id, "-", order["customer"])

# 3. calculate the total amount of completed orders
total_completed = 0
for order in orders.values():
    if order["status"] == "Completed":
        total_completed += order["amount"]

print("\nTotal amount of completed orders:", total_completed)

# 4. Count pending orders
pending_order_count = 0
for order in orders.values():
    if order["status"] == "Pending":
        pending_order_count += 1

print("Number of pending orders:", pending_order_count)

# 5. Add a new order to the dictionary
orders["ORD-004"] = {
    "customer": "Raj",
    "amount": 4500,
    "status": "Completed"
}

# print the updated order
print("\nUpdated Orders:")
for order_id, order in orders.items():
    print(order_id, "-", order)