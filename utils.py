import csv
import json
from config import Config


def csv_to_json(csv_file_path, json_file_path):
    json_data = []

    with open(csv_file_path, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            json_data.append(row)

    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        json_file = json.dumps(json_data, indent=4, ensure_ascii=False)
        jsonf.write(json_file)


csv_to_json(Config.ads_path, Config.ads_pathj)
csv_to_json(Config.categories_path, Config.categories_pathj)
