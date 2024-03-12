from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from suggestion import suggestion_convo

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['conversation_db']
collection = db['samples']

# Define routes for receiving user messages and agent messages
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
        collection.insert_one(conversation_item)
        return jsonify({"status": "Message received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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
        collection.insert_one(conversation_item)
        return jsonify({"status": "Message received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve conversation history
@app.route('/api/conversation', methods=['GET'])
def get_conversation():
    conversation = list(collection.find({}, {'_id': 0}))
    return jsonify(conversation), 200

# Initialize suggestion classifier
classifier = suggestion_convo()

# Route to get suggestions based on the latest message
@app.route('/api/suggestion', methods=['GET'])
def get_suggestion():
    data = list(collection.find({}, {'_id': 0}))
    messg = data[-1]['message']  # Get the latest message from the conversation history
    return jsonify(classifier.suggest(messg))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
    print("Application is running")
