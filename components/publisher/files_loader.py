import os
import json
import random

def get_the_data():
    project_root = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(project_root, "data", "interesting_category.json")
    with open(data_file, mode="r", encoding="utf-8") as f:
        data = json.load(f)
    return  data

