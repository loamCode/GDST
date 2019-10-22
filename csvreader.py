import csv
import matplotlib.pyplot as plt
filename = "gat.csv"

with open(filename) as csv_file:
    reader = csv.reader(csv_file, delimiter=';', lineterminator='\n')
    header_row = next(reader)
    longitude, latitude, = [], []


for index, column_header in enumerate(header_row):
    print(index, column_header)
   

with open(filename) as csv_file:
    reader = csv.reader(csv_file, delimiter=';', lineterminator='\n')
    header_row = next(reader)
    longitude, latitude = [], []
    for row in reader:
        longitude.append(row[0])
        latitude.append(row[1])

