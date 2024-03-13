from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from .suggestion_prediction_model import suggestion_convo
import sys
sys.path.append('./src')
from database_connection import db, collection

suggestion_bp = Blueprint("suggestion", __name__)


# Define routes for receiving user messages and agent messages
@suggestion_bp.route('/user_message', methods=['POST'])
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

@suggestion_bp.route('/agent_message', methods=['POST'])
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

# Route to retrieve conversation history
@suggestion_bp.route('/conversation', methods=['GET'])
def get_conversation():
    conversation = list(collection.find({}, {'_id': 0}))
    return jsonify(conversation), 200

# Initialize suggestion classifier
classifier = suggestion_convo()

# Route to get suggestions based on the latest message
@suggestion_bp.route('/suggestion', methods=['GET'])
def get_suggestion():
    data = list(collection.find({}, {'_id': 0}))
    messg = data[-1]['message']  # Get the latest message from the conversation history
    return jsonify(classifier.suggest(messg))
