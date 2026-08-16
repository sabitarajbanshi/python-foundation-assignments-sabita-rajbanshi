"""
Exercise: Batch Processor
Student: Sabita Rajbanshi 
Day: 2

"""
# loop through batch numbers 1 to 10
for batch_number in range(1, 11):
    print(f"Processing batch {batch_number}")

    # print "Checkpoint reached" for every third batch
    if batch_number % 3 == 0:
        print("Checkpoint reached\n")