#import dependencies pymongo driver
from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

#instantiate Flask
app= Flask(__name__)

#connect to mongodb
#in order to crate a db we must provide both collection and a dummy document
client=MongoClient("mongodb://localhost:27017/")

Datab=client["conversation_d"]
collection=Datab["samples"]


@app.route('/api/user_message', methods=['POST'])
def user_message():
    data = request.json 
    if 'user_id' not in data or 'message' not in data:
        return jsonify({"error": "User ID or message field missing"}), 400
    user_id = data['user_id']
    message = data['message']
    timestamp = datetime.now().isoformat()
    conversation_item = {
        'from': 'user',
        'user_id': user_id,
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
    if 'user_id' not in data or 'message' not in data:
        return jsonify({"error": "User ID or message field missing"}), 400
    user_id = data['user_id']
    message = data['message']
    timestamp = datetime.now().isoformat()
    conversation_item = {
        'from': 'agent',
        'user_id': user_id,
        'message': message,
        'time': timestamp
    }
    try:
        collection.insert_one(conversation_item)
        return jsonify({"status": "Message received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
@app.route('/api/conversation', methods=['GET'])
def get_conversation():
    user_id = request.args.get('user_id')
    if user_id:
        conversation = list(collection.find({'user_id': user_id}, {'_id': 0}))
    else:
        conversation = list(collection.find({}, {'_id': 0}))
    return jsonify(conversation), 200
 
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    print("appln started")