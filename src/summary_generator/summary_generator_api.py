from flask import Flask, request, jsonify
from pymongo import MongoClient
from dialogue_summarizer import DialogueSummarizer

#instantiate flask
app= Flask(__name__)

#instantiate dialoguesummarizer class
summarize= DialogueSummarizer("../../resources/summary/FINE_TUNNED_MODEL_WITH_PEFT")

#connect to MongoDB 
client = MongoClient('mongodb://localhost:27017/')
db = client['conversation_db']
collection = db['samples']

#API for generating summaries
@app.route('/generate_summary',methods=['GET'])
def generate_summary():
    #get dialogues from MongoDB collection
    dialogues=collection.find({},{'_id':0,'from':1,'message':1})

    #extract dialogues as a list from mongo documents
    dialogue_list=[]
    for dialogue in dialogues:
        dialogue_list.append(dialogue['message'])
    try:
        #generate summary using dialogue summarizer class
        generated_summary=summarize.generate_summary(' '.join(dialogue_list))
        return jsonify({"summary":generated_summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#run Flask app
if __name__=='__main__':
    app.run(debug=True)
    print("app is running")

