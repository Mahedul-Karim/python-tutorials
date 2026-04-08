import csv
import pandas

with open("weather_data.csv") as file:
    data = csv.reader(file)
    for row in data:
        print(row)

data = pandas.read_csv("weather_data.csv")
print(data["temp"])