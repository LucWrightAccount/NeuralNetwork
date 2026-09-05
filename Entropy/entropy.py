import csv

with open('data.csv') as file_obj:

    # Create reader object by parssing the file
    # object to reader method
    reader_obj = csv.reader(file_obj)

    for row in reader_obj:
        print(row)