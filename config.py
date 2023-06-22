import os

class Config:
    ads_path = os.path.join("../datasets", "csv_data", "ads.csv")
    ads_pathj = os.path.join("../datasets", "json_data", "ads.json")

    categories_path = os.path.join("../datasets", "csv_data", "categories.csv")
    categories_pathj = os.path.join("../datasets", "json_data", "categories.json")

    data_path_cat = os.path.join("./datasets/json_data/categories.json")
    data_path_ads = os.path.join("./datasets/json_data/ads.json")