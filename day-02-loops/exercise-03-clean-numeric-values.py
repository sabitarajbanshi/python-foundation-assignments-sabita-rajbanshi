"""
Exercise: Clean Numeric Values
Student: Sabita Rajbanshi 
Day: 2

"""
# list containing integers, strings, and None values
raw_values = [100, None, 250, "invalid", 300, None, 450]

# Approach 1: using loop
clean_values = []
for value in raw_values:
    if not isinstance(value, int):  # skip the value if it is not an integer
        continue
    clean_values.append(value)
print(f"Clean numeric values using loop: {clean_values}")

# Approach 2: using list comprehension

clean_values_lc = [value for value in raw_values if isinstance(value, int)]
print(f"Clean numeric values using list comprehension: {clean_values_lc}")