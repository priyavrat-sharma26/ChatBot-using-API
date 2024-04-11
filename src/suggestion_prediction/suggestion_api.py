from flask import Blueprint, request, jsonify
from .suggestion_prediction_model import suggestion_convo
import sys
sys.path.append('./src')
from src.database_connection import collection

suggestion_bp = Blueprint("suggestion", __name__)


# Initialize suggestion classifier
classifier = suggestion_convo()

data = list(collection.find({}, {'_id': 0}))
last_user_message = None
for message in data:
    if message["from"] == "user":
        if last_user_message is None or message["time"] > last_user_message["time"]:
            last_user_message = message

# Route to get suggestions based on the latest message
@suggestion_bp.route('/suggestion', methods=['GET'])
def get_suggestion():
    messg = last_user_message['message']  # Get the latest user message from the conversation history
    return jsonify(classifier.suggest(messg))
