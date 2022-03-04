from pymongo import MongoClient

client = MongoClient()

# 'mongodb+srv://isaacrobert:ayowumi33@cluster0.z1j5f.mongodb.net/CMS?keepAlive=true&autoReconnect=true&socketTimeoutMS=360000&connectTimeoutMS=360000&retryWrites=true&w=majority')


class AdminModel:
    def __init__(self) -> None:
        self.db = client

    def create(self, colname, dataset: dict):
        #Creates Collections with collection name and the dataset as params
        
        ncol = self.db[colname]
        self.insert(dataset, colname)
        return self.get_data(colname)

    def insert(self, data: dict, colname):
        #Inserts data into a collection with the data and collection name as params

        col = self.db[colname]
        col.insert_one(data)
        return self.get_data()
    
    def insert_many(self, dataset: list, colname):
        col = self.db[colname]
        col.insert_many(dataset)
        return self.get_data(colname)

    def update(self, ID, data: dict, colname):
        #Updates data in a collections with the collection name, ID and data as params

        col = self.db[colname]
        col.find_one_and_update({'_id': ID}, {"$set": data}, upsert=0)
        return self.get_data(colname)

    def delete(self, data: dict, colname):
        #Deletes data in a collection with the collection's name and data

        col = self.db[colname]
        col.delete_one(data)
        return self.get_data(colname)

    def get_data(self, colname):
        col = self.db[colname]
        cr = col.find({})
        return list(cr)
    
    def get_cols(self):
        return list(self.db.list_collection_names())

# AdminModel().get_cols()
