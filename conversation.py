from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["conversation_db"]
collection = db["conversation_history"]

# Endpoint to receive user messages and update conversation
@app.route('/api/user_message', methods=['POST'])
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
        collection.update_one({}, {'$push': {'conversation': conversation_item}}, upsert=True)
        return jsonify({"status": "Message received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to receive agent messages and update conversation
@app.route('/api/agent_message', methods=['POST'])
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
        collection.update_one({}, {'$push': {'conversation': conversation_item}}, upsert=True)
        return jsonify({"status": "Message received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve entire conversation history
@app.route('/api/conversation_history', methods=['GET'])
def get_conversation_history():
    try:
        conversation_history = collection.find_one({}, {'_id': 0})
        return jsonify(conversation_history), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    print("Application is running")
