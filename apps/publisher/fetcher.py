import os
import json
import random


class Fetcher:

    def get_the_data(self):
        project_root = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(project_root, "data", "newsgroups_interesting.json")
        with open(data_file, mode="r", encoding="utf-8") as f:
            data = json.load(f)
        num = random.randint(0, 1000)
        for i in range (num):
            print(data[i])




