from flask import Flask, jsonify, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URI = os.getenv("DATABASE_URI")
if not DATABASE_URI:
    raise ValueError("DB_URI is not set in the .env file")

client = MongoClient(DATABASE_URI)
db = client["zuAi"]
collection = db["assessment"]
print(collection)

# Flask app setup
app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/api/data", methods=["GET"])
def get_all_data():
    try:
        data = list(collection.find({}, {"_id": 0}))
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
