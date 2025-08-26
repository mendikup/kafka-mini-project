import os
import json


class Loader:
    @staticmethod
    def get_interesting_data():
        project_root = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(project_root, "data", "interesting_category.json")
        with open(data_file, mode="r", encoding="utf-8") as f:
            data = json.load(f)
        return  data

    @staticmethod
    def get_not_interesting_data():
        project_root = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(project_root, "data", "not_intersting_category_dict.json")
        with open(data_file, mode="r", encoding="utf-8") as f:
            data = json.load(f)
        return  data




