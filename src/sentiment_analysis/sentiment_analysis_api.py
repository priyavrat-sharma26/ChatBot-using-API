from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['conversation_db']
collection = db['samples']

# Importing the SentimentAnalysis class from Sentiment_analysis module
from Sentiment_analysis import SentimentAnalysis

# Creating an instance of the SentimentAnalysis class
classifier = SentimentAnalysis()

# API route for getting sentiment analysis
@app.route('/api/sentiment', methods=['GET'])
def get_sentiment():
    # Fetching data from MongoDB collection
    data = list(collection.find({}, {'_id': 0}))
    user_msg_list = []

    # Extracting user messages from the fetched data
    for i in data:
        if i["from"] == "user":
            user_msg_list.append(i["message"])

    # Selecting the last five user messages
    last_five_msg = user_msg_list[-5:]

    # Combining last five messages into a single string
    msg_string = ".".join(last_five_msg)

    # Performing sentiment analysis on the combined messages
    sentiment = classifier.give_sentiment(msg_string)

    # Returning sentiment analysis result as JSON response
    return jsonify(sentiment), 200

if __name__ == '__main__':
    # Running the Flask application
    app.run(debug=True)
    print("Application is running")
