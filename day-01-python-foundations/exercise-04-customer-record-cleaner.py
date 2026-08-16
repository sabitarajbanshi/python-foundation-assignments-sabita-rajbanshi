"""
Exercise: Customer record cleaner
Student: Sabita Rajbanshi
Day: 1

"""

# Variables: customer information
raw_name = " sAgar THAPA"
raw_city = "KATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

# Data Cleaning
name = raw_name.strip().title() # converting to title case removing extra spaces
city = raw_city.strip().title()
age = int(raw_age) # convert age from string to integer
email = raw_email.strip().lower() # convert to lowercase

# ternary expression to determine status
status = "Adult" if age >= 18 else "Minor"

# output for cleaned customer information
print("Name: ", name)
print("City: ", city)
print("Age: ", age)
print("Email: ", email)
print("Status: ", status)