from pymongo.mongo_client import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDBConnection:
    def _init_(self, uri, database_name):
        self.uri = uri
        self.database_name = database_name

    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.database_name]
            self.client.admin.command('ismaster')
            print("MongoDB connection successful")
        except ConnectionFailure:
            print("Could not connect to MongoDB")

    def get_specific_data(self, collection_name, query):
        collection = self.db[collection_name]
        result = collection.find_one(query)
        return result

# Usage
uri = "mongodb://client:client@ac-e4tecns-shard-00-00.ffbi8oh.mongodb.net:27017,ac-e4tecns-shard-00-01.ffbi8oh.mongodb.net:27017,ac-e4tecns-shard-00-02.ffbi8oh.mongodb.net:27017/?ssl=true&replicaSet=atlas-dhu2oe-shard-0&authSource=admin&retryWrites=true&w=majority"
database_name = "PolyglotSystem"  
db = MongoDBConnection(uri, database_name)
db.connect()

collection_name = "clients" 
query = {"CustomerId": 1}

result = db.get_specific_data(collection_name, query)
print(result)