# Import necessary libraries
from transformers import BertTokenizer, BertForNextSentencePrediction
# import torch
import nltk
import pandas as pd

# Download NLTK data
nltk.download('punkt')

# Load BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForNextSentencePrediction.from_pretrained('bert-base-uncased')

# Read data from Excel file
df = pd.read_excel('resources/suggestion_prediction/sentences.xlsx')
sentences = df.iloc[:, 0].tolist()

# Define a class for suggesting conversations
class suggestion_convo:
    def __init__(self):
        # Initialize tokenizer and model within the class
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertForNextSentencePrediction.from_pretrained('bert-base-uncased')
        
    # Function to predict the probability of the next sentence
    def predict_next_sentence(self, sentence1, sentence2):
        tokens = self.tokenizer(sentence1, sentence2, return_tensors='pt')
        probabilities = self.model(**tokens).logits
        # probabilities = torch.softmax(logits, dim=1)
        return probabilities[:, 0].item()
      
    # Function to suggest conversations based on a given message
    def suggest(self, message):
        probabilities = [self.predict_next_sentence(message, i) for i in sentences]
        indexed_list = list(enumerate(probabilities))
        sorted_indices = sorted(indexed_list, key=lambda x: x[1], reverse=True)[:3]
        largest_indices = [index for index, value in sorted_indices]
        suggestions = [sentences[i] for i in largest_indices]
        return suggestions
