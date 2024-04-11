
from flask import Blueprint, jsonify
from pymongo import MongoClient
from src.next_sentence_prediction_gpt2.gp2_nsp_model import NextSentencePrediction  # Assuming this imports your summarizer class
from database_connection import db, collection
 
suggestion_gpt2_bp = Blueprint("suggestion_gpt2", __name__)
 
# Instantiate dialoguesummarizer class (assuming it has a constructor)
predictor = NextSentencePrediction()
 
@suggestion_gpt2_bp.route('/next_sentence', methods=['GET'])
def next_sentence():
    try:
        # Get dialogues from MongoDB collection
        data = list(collection.find({}, {'_id': 0}))
        last_user_message = None
        for message in data:
            if message["from"] == "user":
                if last_user_message is None or message["time"] > last_user_message["time"]:
                    last_user_message = message

           
        next_sentence = predictor.generate_agent_responses(last_user_message)
        return jsonify(next_sentence), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500