"""
Exercise: File Validator
Student: Sabita Rajbanshi
Day: 1

"""

# input method to get a file name 
file_name = input("Enter a file name: ")

# data cleaning: removing extra spaces using strip() and converting to lowercase using lower()
file_name = file_name.strip().lower()

# allowed file extensions
extensions = (".csv", ".json", ".parquet")

# validate the file name against given file extensions
if file_name.endswith(extensions):
    print(f"Dataset: {file_name}")
else:
    print(f"Invalid dataset: {file_name}")


