from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from database_connection import db, collection
 
conversation_bp = Blueprint("conversation", __name__)
 

 
@conversation_bp.route('/user_message', methods=['POST'])
def user_message():
    data = request.json
    if 'message' not in data:
        return jsonify({"error": "Message field missing"}), 400
    message = data['message']
    timestamp = datetime.now().isoformat()
    conversation_item = {
        'from': 'user',
        'message': message,
        'time': timestamp
    }
    try:
        collection.insert_one(conversation_item)
        return jsonify({"status": "Message received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
@conversation_bp.route('/agent_message', methods=['POST'])
def agent_message():
    data = request.json
    if 'message' not in data:
        return jsonify({"error": "Message field missing"}), 400
    message = data['message']
    timestamp = datetime.now().isoformat()
    conversation_item = {
        'from': 'agent',
        'message': message,
        'time': timestamp
    }
    try:
        collection.insert_one(conversation_item)
        return jsonify({"status": "Message received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
@conversation_bp.route('/conversation', methods=['GET'])
def get_conversation():
    conversation = list(collection.find({}, {'_id': 0}))
    return jsonify(conversation), 200
