from pymongo import MongoClient
from scraper.schema_validator import validate_assessment
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URI = os.getenv('DATABASE_URI')
if not DATABASE_URI:
    raise ValueError("DB_URI is not set in the .env file")


client = MongoClient(DATABASE_URI)
db = client["zuAi"]
collection = db["assessment"]
print(collection)

def upsert_valid_data(scraped_data):
    for entry in scraped_data:
        if validate_assessment(entry):
            filter_query = {"assessment_id": entry["assessment_id"]}
            update_query = {"$set": entry}
            result = collection.update_one(filter_query, update_query, upsert=True)
            if result.upserted_id:
                print(f"Document inserted with ID: {result.upserted_id}")
            else:
                print(f"Document with ID {entry['assessment_id']} updated successfully.")
        else:
            print(f"Skipping invalid entry: {entry}")