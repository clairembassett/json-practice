#!/usr/bin/env python3
import json
import csv

file_path = '/Users/clairebassett/json-practice/data/schacon.repos.json'
csv_file_path = 'chacon.csv'

with open(file_path, 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    count = 0
    for item in data:
        if count < 5:
            name = item.get("name")
            html_url = item.get("html_url")
            updated_at = item.get("updated_at")
            visibility = item.get("visibility")
            count += 1
            csvwriter.writerow([name, html_url, updated_at, visibility])
        else:
            break

print('CSV file created successfully.')


