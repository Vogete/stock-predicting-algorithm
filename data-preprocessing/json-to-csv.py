import csv
import json

json_filename = 'mock-news-data.json'
csv_filename = 'mock-news-data.csv'
columns = ['title', 'content', 'date', 'newscompany']
includes_header = False

with open(json_filename) as file:
    data = json.load(file)

with open(csv_filename, "w") as file:
    csv_file = csv.writer(file)
    if includes_header == True:
        csv_file.writerow(columns)

    for item in data:
        row = []
        for column in columns:
            row.append(item[column])

        csv_file.writerow(row)
