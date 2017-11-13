import csv
import json

json_filename = 'mock-news-data.json'
csv_filename = 'mock-news-data.csv'
includes_header = True

with open(json_filename) as file:
    data = json.load(file)

with open(csv_filename, "w") as file:
    csv_file = csv.writer(file)
    if includes_header == True:
        csv_file.writerow(['title', 'content', 'date', 'newscompany'])

    for item in data:
        csv_file.writerow([item['title'], item['content'], item['date'], item['newscompany']])