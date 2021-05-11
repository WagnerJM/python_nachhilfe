import csv

file = open('data/data.csv', 'r')

csv_data = csv.reader(file, delimiter=";")

csv_data = csv.reader(open('data/data.csv', 'r'), delimiter=';')

for data in csv_data:
    print(f'Zeit: {data[5]} Temp: {data[6]}')



