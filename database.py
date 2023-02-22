from pymongo import MongoClient
from flask import Flask 

MONGO_URI = "mongodb://localhost:27017/"
app = Flask(__name__)

client = MongoClient(MONGO_URI)

db = client["INTRANET"]

if __name__ == "__main__":
    app.run(debug=True, port=5500)

