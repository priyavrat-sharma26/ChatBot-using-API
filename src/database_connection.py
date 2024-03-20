
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://saket07singh:Fetjmi1920@clustersaket.80ewjt5.mongodb.net/?retryWrites=true&w=majority&appName=Clustersaket"


#client = MongoClient('mongodb://localhost:27017/')
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['conversation_db']
collection = db['samples']
