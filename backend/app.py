
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import os

app = Flask(__name__)

# MongoDB connection
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://mongodb:27017/"
)

client = MongoClient(MONGO_URI)
db = client["todo_database"]
todo_collection = db["todo_items"]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "success": True,
        "message": "Flask backend is running"
    })


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():

    data = request.get_json(silent=True) or {}

    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({
            "success": False,
            "message": "Item Name and Description are required"
        }), 400

    todo = {
        "itemName": item_name.strip(),
        "itemDescription": item_description.strip()
    }

    result = todo_collection.insert_one(todo)

    return jsonify({
        "success": True,
        "message": "To-Do item saved successfully",
        "itemId": str(result.inserted_id)
    }), 201


@app.route("/items", methods=["GET"])
def get_items():

    todos = list(todo_collection.find())

    for todo in todos:
        todo["_id"] = str(todo["_id"])

    return jsonify(todos)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
