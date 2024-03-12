# Importing the pipeline class from the transformers library
from transformers import pipeline

# Defining a class for sentiment analysis
class SentimentAnalysis():
    # Constructor to initialize the sentiment analysis pipeline
    def __init__(self, model_name="j-hartmann/emotion-english-distilroberta-base"):
        # Creating a pipeline for text classification using the specified model
        self.classifier_roberta = pipeline("text-classification", model=model_name)
    
    # Method to perform sentiment analysis on a given message
    def give_sentiment(self, message):
        # Calling the pipeline to classify the sentiment of the message
        # Extracting the sentiment label from the classification result
        return list(self.classifier_roberta(message)[0].values())[0]
