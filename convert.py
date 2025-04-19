import csv
import json

with open('products.csv', mode='r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    products = list(reader)

with open('products.json', mode='w', encoding='utf-8') as json_file:
    json.dump(products, json_file, indent=2, ensure_ascii=False)

print("Konvertierung erfolgreich! → products.json")
