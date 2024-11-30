from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["assessment_db"]
collection = db["assessments"]


def upsert_to_mongodb(data):
    filter_query = {"assessment_id": data["assessment_id"]}
    update_query = {"$set": data}
    result = collection.update_one(filter_query, update_query, upsert=True)
    if result.upserted_id:
        print(f"Document inserted with ID: {result.upserted_id}")
    else:
        print("Document updated successfully.")
