#!/usr/bin/env python
# coding: utf-8

# In[7]:


from transformers import pipeline
class SentimentAnalysis():
    def __init__(self,model_name="j-hartmann/emotion-english-distilroberta-base"):
        self.classifier_roberta = pipeline("text-classification", model=model_name)
    def give_sentiment(self,message):
        return (list(self.classifier_roberta(message)[0].values())[0])

