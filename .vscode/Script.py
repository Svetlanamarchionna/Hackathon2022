import csv

with open('metadata.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    print(csv_reader)