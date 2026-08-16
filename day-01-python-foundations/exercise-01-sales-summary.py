
"""
Exercise: Sales Summary
Student: Sabita Rajbanshi
Day: 1
"""

# Input values for the product
product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10

# Calculation for gross sales before discount
gross_sales = unit_price * quantity_sold

# Calculation for the discount amount
discount_amount = gross_sales * discount_percentage

# Calculation for the final sales amount after discount
final_sales_amount = gross_sales - discount_amount

# outputs using f-string
print(f"Product: {product_name}")
print(f"Gross sales: NPR {gross_sales:.2f}")
print(f"Discount: NPR {discount_amount:.2f}")
print(f"Final sales: NPR {final_sales_amount:.2f}")