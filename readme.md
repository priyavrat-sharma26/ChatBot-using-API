# LLM Module

## Hugging Face for Sentiment Analysis:
### j-hartmann/emotion-english-distilroberta-base
This model is designed for sentiment analysis, specifically focusing on English text. It utilizes the DistilRoBERTa architecture, which is a distilled version of the RoBERTa model, known for its strong performance in natural language understanding tasks. The model is trained to classify text into various emotion categories, enabling it to determine the sentiment expressed in a given piece of text, whether it's positive, negative, neutral, or belongs to a specific emotional category.

## Suggestion Prediction:
The provided code serves the purpose of generating conversation suggestions based on a given message using BERT (Bidirectional Encoder Representations from Transformers) model. Here's a short description of the requirements for this code:

**Transformers Library**: The code requires the transformers library to be installed. This library provides pre-trained models for natural language understanding tasks like tokenization and next sentence prediction.

NLTK Data: NLTK (Natural Language Toolkit) is used for tokenization. The code downloads necessary NLTK data using nltk.download('punkt').

BertTokenizer and BertForNextSentencePrediction: The code uses the BertTokenizer to tokenize input text and BertForNextSentencePrediction model to predict the likelihood of the next sentence given two input sentences. These components are loaded from the transformers library.

Data Source: The code requires an Excel file named sentences.xlsx containing a list of sentences. These sentences serve as potential responses or continuations in a conversation.

Suggestion Convo Class: The suggestion_convo class encapsulates the functionality for generating conversation suggestions. It contains methods to initialize the tokenizer and model, predict the probability of the next sentence given a message, and suggest conversations based on a given message.

Flask Application: The code integrates with a Flask web application to provide an API for receiving user messages, storing them in a MongoDB database, retrieving conversation history, and generating conversation suggestions based on the latest message.

MongoDB Database: The code assumes the presence of a MongoDB database named conversation_db and a collection named samples for storing conversation messages.

## Summary Generator:
### T5 & LoRA Fine tunning
T5ForConditionalGeneration is a model based on the T5 (Text-To-Text Transfer Transformer) architecture, which is proficient in various natural language processing tasks, including summarization. This model is trained to generate summaries of input text based on a provided prompt or conditioning. It works in a text-to-text manner, meaning both the input and output are represented as text strings. Given a piece of text and a desired length or objective, the model generates a concise summary that captures the key information or main points from the input text. This capability makes it highly useful for automating the summarization process across different domains and applications


### Note
resources folder contain requierd files and module
