from pymongo import MongoClient


CONNECTION_STRING = "mongodb+srv://technova:additi123@cluster0.aw8c8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(CONNECTION_STRING)
db = client['data']
users_collection = db['users']


