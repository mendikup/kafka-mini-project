from pymongo import MongoClient
import os
from dotenv import load_dotenv

class Dal:

    load_dotenv()


    def __init__(self, collection_name="interesting"):
        self.db = None
        self.database = os.getenv("MONGO_DB")
        self.collection = collection_name

    def insert_data(self, document) -> dict:
        uri = os.getenv("MONGO_URI")
        with MongoClient(uri) as client:
            self.db = client[self.database]
            collection = self.db[self.collection]
            result = collection.insert_one(document)
            if result.inserted_id:
                return {"msg": f"inserted successfully. _id: {result.inserted_id}"}
            return {"msg": "there is is a problem inserting the data"}

    def get_all_data(self):
        uri = os.getenv("MONGO_URI")
        with MongoClient(uri) as client:
            self.db = client[self.database]
            collection = self.db[self.collection]
            result = list(collection.find({}))
            return result
