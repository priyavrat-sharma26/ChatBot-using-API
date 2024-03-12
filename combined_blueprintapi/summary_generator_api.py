from flask import Blueprint, jsonify
from pymongo import MongoClient
from summary_generator_model import DialogueSummarizer
from database_connection import db, collection
 
summary_bp = Blueprint("summary", __name__)

# Instantiate dialoguesummarizer class
summarize = DialogueSummarizer("resources/summary/FINE_TUNNED_MODEL_WITH_PEFT")
 
 
# API for generating summaries
@summary_bp.route('/generate_summary', methods=['GET'])
def generate_summary():
    # Get dialogues from MongoDB collection
    dialogues = collection.find({}, {'_id': 0, 'from': 1, 'message': 1})
 
    # Extract dialogues as a list from mongo documents
    dialogue_list = []
    for dialogue in dialogues:
        dialogue_list.append(dialogue['message'])
    try:
        # Generate summary using dialogue summarizer class
        generated_summary = summarize.generate_summary(' '.join(dialogue_list))
        return jsonify({"summary": generated_summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
