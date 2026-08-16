"""
Exercise: Retry simulation
Student: Sabita Rajbanshi 
Day: 2

"""
# scenarios: 
test_cases = [
    ("Case 1: Success on attempt 2", 2), # label, attempt number that succeeds
    ("Case 2: Failure after three attempts", 0)
]

# loop through each cases
for test_case, success_on_attempt in test_cases:
    print(test_case)

    # Variables
    attempt = 1
    max_attempts = 3
    operation_successful = False

    # loop through maximum allowed retry attempts
    while attempt <= max_attempts:
        print(f"Attempt {attempt}")

        # check if this attempt should succeed
        if attempt == success_on_attempt:
            operation_successful = True

        # stop retrying early if the operation succeeded 
        if operation_successful:
            break

        # move to the next attempt
        attempt += 1

    # Final result
    if operation_successful:
        print("Operation completed successfully")
    else:
        print("Operation failed after 3rd attempts")
