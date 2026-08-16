"""
Exercise: Data Quality Checker
Student: Sabita Rajbanshi
Day: 1
"""

# Input values for the dataset
total_rows = 2000
missing_rows = 120
duplicate_rows = 30

# Calculation for total problematic rows (missing and duplicate rows do not overlap)
total_problematic_rows = missing_rows + duplicate_rows

# Calculation for the percentage of problematic rows
problematic_percentage = (total_problematic_rows / total_rows) * 100

# Classify the dataset based on three different categories
if problematic_percentage <= 2:
    classification = "Excellent"
elif problematic_percentage <= 5:
    classification = "Acceptable"
else:
    classification = "Needs Cleaning"

# Output using f-string
print("Total rows: ", total_rows)
print("Problematic rows: ", total_problematic_rows)
print("Problem percentage: ", problematic_percentage)
print("Final classification: ", classification)
