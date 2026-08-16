"""
Exercise: Sales list analysis
Student: Sabita Rajbanshi 
Day: 2

"""
# list of monthly sales
monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

# 1. sorted sales from highest to lowest
sorted_sales = sorted(monthly_sales, reverse=True)

# 2. filter sales amount above 100,000 using list comprehension
sales_above_100k = [amount for amount in monthly_sales if amount > 100000]

# 3. adding 13% tax to monthly sales amount
sales_with_tax = [amount * 1.13 for amount in monthly_sales]

# 4. total sales amount
total_sales = sum(monthly_sales)

# 5. average sales amount
average_sales = total_sales / len(monthly_sales)

# outputs
print(f"Sorted sales from highest to lowest: {sorted_sales}\n")
print(f"Sales above 100000: {sales_above_100k}\n")
print(f"Sales with 13% tax: {sales_with_tax}\n")
print(f"Total sales: {total_sales: .2f}\n")
print(f"Average sales: {average_sales: .2f}")
