from flask import Blueprint, jsonify
from pymongo import MongoClient
from .sentiment_analysis_model import SentimentAnalysis 
from database_connection import db, collection 
sentiment_bp = Blueprint("sentiment", __name__)
 
 
classifier = SentimentAnalysis()
 
@sentiment_bp.route('/sentiment', methods=['GET'])
def get_sentiment():
    data = list(collection.find({}, {'_id': 0}))
    user_msg_list = [i["message"] for i in data if i.get("from") == "user"]
    last_five_msg = user_msg_list[-5:]
    msg_string = ".".join(last_five_msg)
    sentiment = classifier.give_sentiment(msg_string)
    return jsonify(sentiment), 200
