"""
Exercise: Dataset comparison
Student: Sabita Rajbanshi 
Day: 2

"""
# given two datasets
dataset_a = {"customer", "sales", "product", "employee"}
dataset_b = {"sales", "product", "supplier", "inventory"}

# union method for finding unique dataset names from two different datasets
unique_datasets = dataset_a.union(dataset_b)

# intersection menthod for finding common dataset names from two different datasets
common_datasets = dataset_a.intersection(dataset_b)

# dataset names only in dataset_a
dataset_only_in_a = dataset_a - dataset_b

# dataset names only in dataset_b
datasets_only_in_b = dataset_b - dataset_a

# outputs
print(f"All unique dataset names: {unique_datasets}\n")
print(f"Datasets found in both groups: {common_datasets}\n")
print(f"Datasets only in dataset_a: {dataset_only_in_a}\n")
print(f"Datasets only in dataset_b: {datasets_only_in_b}")