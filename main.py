import csv

# Normal data
data = []

# Read
with open("dataset_2.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

# Data for headers and planet data
headers = data[0]
planet_data = data[1:]

#Converting all planet names to lower case
for data_point in planet_data:
    data_point[2] = data_point[2].lower()

#Sorting planet names in alphabetical order
planet_data.sort(key=lambda planet_data: planet_data[2])

# Create csv file
with open("dataset_2_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)