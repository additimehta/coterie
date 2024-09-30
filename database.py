from pymongo import MongoClient


CONNECTION_STRING = YOUR_CONNECTION_STRING
client = MongoClient(CONNECTION_STRING)
db = client['data']
users_collection = db['users']


