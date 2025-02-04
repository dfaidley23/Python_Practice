import csv

with open("files/weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

#modify or open csvs. This will search the csv and access the city in the 0 index and then return the temperature in the 1 index
#[1:] will simply cut off the 0 index item in the csv and search the rest
for row in data[1:]:
    if row[0] == city:
        print(row[1])