from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from src.database_connection import db, collection
from src.Next_Best_Action.class_fine_tuned_gpt import NextBestActionPredictor
 
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



@conversation_bp.route('/clear_conversation', methods=['DELETE'])
def clear_conversation():
    try:
        collection.delete_many({})  # Delete all documents in the collection
        return jsonify({"status": "Conversation cleared"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
 
 
action_predictor = NextBestActionPredictor()
@conversation_bp.route('/next_best_action', methods=['POST'])
def next_best_action():
    data = request.json
    if 'summary' not in data:
        return jsonify({"error": "summary field missing"}), 400
    message = data['summary']
    next_action = action_predictor.predict_action(message)
    return jsonify({"action": next_action}), 200