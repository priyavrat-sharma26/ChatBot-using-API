
from transformers import BertTokenizer, BertForNextSentencePrediction
import torch
import nltk
import pandas as pd




nltk.download('punkt')

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForNextSentencePrediction.from_pretrained('bert-base-uncased')


df = pd.read_excel('sentences.xlsx')
sentences = df.iloc[:, 0].tolist()



class suggestion_convo:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertForNextSentencePrediction.from_pretrained('bert-base-uncased')
        
    
    def predict_next_sentence(self, sentence1, sentence2):
        tokens = self.tokenizer(sentence1, sentence2, return_tensors='pt')
        logits = self.model(**tokens).logits
        probabilities = torch.softmax(logits, dim=1)
        next_sentence_probability = probabilities[:, 0].item()
        return next_sentence_probability
      
    def suggest(self, message):
        probabilities = [self.predict_next_sentence(message, i) for i in sentences]
        indexed_list = list(enumerate(probabilities))
        sorted_indices = sorted(indexed_list, key=lambda x: x[1], reverse=True)[:5]
        largest_indices = [index for index, value in sorted_indices]
        suggestions = [sentences[i] for i in largest_indices]
        return suggestions



    



