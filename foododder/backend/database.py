from pymongo import MongoClient
import os

MONGO_URL = "mongodb+srv://navonilsaha4_db_user:12345@cluster0.e9m2r0o.mongodb.net/"

client = MongoClient(MONGO_URL)

db = client["moodbites"]

users_collection = db["users"]
restaurants_collection = db["restaurants"]
foods_collection = db["foods"]