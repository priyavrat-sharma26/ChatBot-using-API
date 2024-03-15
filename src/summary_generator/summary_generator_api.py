
from flask import Blueprint, jsonify
from pymongo import MongoClient
from .summary_generator_model import DialogueSummarizer  # Assuming this imports your summarizer class
from database_connection import db, collection
 
summary_bp = Blueprint("summary", __name__)
 
# Instantiate dialoguesummarizer class (assuming it has a constructor)
summarize = DialogueSummarizer("resources/summary/FINE_TUNNED_MODEL_WITH_PEFT")
 
 
@summary_bp.route('/generate_summary', methods=['GET'])
def generate_summary():
    try:
        # Get dialogues from MongoDB collection
        dialogues = list(collection.find({}, {'_id': 0}))
 
        messages = []
 
        for dialogue in dialogues:
            if dialogue.get("from") == "user":
                messages.append("User: " + dialogue["message"])
            elif dialogue.get("from") == "agent":
                messages.append("Agent: " + dialogue["message"])
   
        print(messages)      
        generated_summary = summarize.generate_summary(messages)
        
        
        
        return jsonify({"summary": generated_summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
