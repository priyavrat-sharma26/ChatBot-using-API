
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
 
        # Prepare a list to store individual summaries
        generated_summaries = []
 
        # Process each dialogue separately and generate summary
        for dialogue in dialogues:
            if dialogue.get("from") == "user":
                # Start new dialogue
                current_dialogue = [dialogue["message"]]
            elif dialogue.get("from") == "agent":
                # Add agent message to current dialogue
                current_dialogue.append("Agent: " + dialogue["message"])
                # Generate summary for the current dialogue
                generated_summary = summarize.generate_summary(current_dialogue)
                # Append generated summary to the list
                generated_summaries.append(generated_summary)
 
        # Join all summaries into a single string
        final_summary = " ".join(generated_summaries)
 
        return jsonify({"summary": final_summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500