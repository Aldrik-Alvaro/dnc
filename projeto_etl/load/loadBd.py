from pymongo import MongoClient

class Load:
    def __init__(self, db_name):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
    def upsert_dataframe(self, df, upsert_key, collection_name):
        for _, row in df.iterrows():
            unique_key = row[upsert_key]
            data = row.to_dict()
            self.collection = self.db[collection_name]
            self.collection.update_one({'hashId': unique_key}, {'$set': data}, upsert=True)

