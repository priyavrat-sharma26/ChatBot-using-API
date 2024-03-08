from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['conversation_db']
collection = db['samples']

from Sentiment_analysis import SentimentAnalysis
classifier = SentimentAnalysis()
@app.route('/api/sentiment', methods=['GET'])
def get_sentiment():
    data = list(collection.find({}, {'_id': 0}))
    user_msg_list = []
    for i in data:
        if (i["from"]) == "user":
            user_msg_list.append(i["message"])
            # sentiment = classifier.give_sentiment(user_msg_list[-1])
    last_five_msg = user_msg_list[len(user_msg_list)-5::]
    msg_string = ".".join(last_five_msg)
    sentiment = classifier.give_sentiment(msg_string)
    return jsonify(sentiment), 200

if __name__ == '__main__':
    app.run(debug=True)
    print("Application is running")
