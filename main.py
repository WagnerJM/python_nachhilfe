import csv

file = open('data/data.csv', 'r')

csv_data = csv.reader(file, delimiter=";")

csv_data = csv.reader(open('data/data.csv', 'r'), delimiter=';')

for data in csv_data:
    print(f'Zeit: {data[5]} Temp: {data[6]}')



"""
[
   [3660, DHT22, 1846, 51.482, 7.224, 2021-04-26T00:01:56, 5.60,99.90],
   [......] 
]

"""