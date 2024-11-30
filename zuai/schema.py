from pymongo import MongoClient, UpdateOne
from jsonschema import validate, ValidationError

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["assessment_db"]
collection = db["assessments"]

# Define JSON schema
assessment_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "title": "Assessment",
    "properties": {
        "assessment_id": {"type": "string"},
        "title": {"type": "string"},
        "description": {"type": "string"},
        "subject": {"type": "string"},
        "word_count": {"type": "integer"},
        "read_time": {"type": "string"},
        "publication_date": {
            "type": "string",
            "pattern": "^(\\d{4}/\\d{2}/\\d{2}|NA)$",
        },
        "details": {
            "type": "object",
            "properties": {
                "author": {"type": "string"},
                "difficulty_level": {"type": "string"},
                "keywords": {"type": "array", "items": {"type": "string"}},
            },
            "additionalProperties": True,
        },
    },
    "required": [
        "assessment_id",
        "title",
        "description",
        "subject",
        "word_count",
        "read_time",
        "publication_date",
    ],
    "additionalProperties": False,
}


# Validation function
def validate_assessment(data):
    try:
        validate(instance=data, schema=assessment_schema)
        return True
    except ValidationError as e:
        print(f"Validation Error: {e}")
        return False


def upsert_assessment(data):
    if validate_assessment(data):
        filter_query = {"assessment_id": data["assessment_id"]}
        update_query = {"$set": data}
        result = collection.update_one(filter_query, update_query, upsert=True)
        if result.upserted_id:
            print(f"Document inserted with ID: {result.upserted_id}")
        else:
            print("Document updated successfully.")
    else:
        print("Invalid data. Upsert operation aborted.")
