"""
Exercise:  Dataset access decision
Student: Sabita Rajbanshi
Day: 1

"""
# roles allowed to access datasets
allowed_roles = ["analyst", "scientist", "engineer"]

# datasets that are restricted
restricted_datasets = ["salary_data", "personal_data"]

# test cases: (user_role, is_active, requested_data)
test_cases = [
    ("analyst", True, "sales_data"),
    ("analyst", False, "sales_data"),
    ("scientist", True, "personal_data"),
    ("AI engineer", True, "salary_data"),
    ("engineer", True, "sales_data")
]
# checking for access by looping through each test case
for user_role, is_active, requested_data in test_cases:
  print(f"Role: {user_role}, Active: {is_active}, Dataset: {requested_data}")


  if not is_active:   # deny access if the user is inactive
      print("Result: Access denied because the user is inactive.\n")
  elif user_role not in allowed_roles:   # deny access if the role is not allowed to access dataset
      print("Result: Access denied because the role is not allowed.\n")
  elif requested_data in restricted_datasets:   # deny access if the requested dataset is restricted
      print("Result: Access denied because the dataset is restricted.\n")
  else:  # grant access only if all conditions meet
      print("Result: Access granted.\n")