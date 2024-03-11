# LLM Module

## Hugging Face for Sentiment Analysis:
### j-hartmann/emotion-english-distilroberta-base
This model is designed for sentiment analysis, specifically focusing on English text. It utilizes the DistilRoBERTa architecture, which is a distilled version of the RoBERTa model, known for its strong performance in natural language understanding tasks. The model is trained to classify text into various emotion categories, enabling it to determine the sentiment expressed in a given piece of text, whether it's positive, negative, neutral, or belongs to a specific emotional category.

## Suggestion Prediction:
### Bert
BertForNextSentencePrediction is a model designed for predicting whether one sentence follows another in a given context. This model is built on the BERT (Bidirectional Encoder Representations from Transformers) architecture, which is pre-trained on large corpora of text data. It is particularly useful for tasks like question answering, dialogue generation, and contextual understanding. Given a pair of sentences, the model predicts whether the second sentence logically follows the first one or not, making it valuable for generating suggestions or completing prompts in various natural language processing applications.

## Summary Generator:
### T5 & LoRA Fine tunning
T5ForConditionalGeneration is a model based on the T5 (Text-To-Text Transfer Transformer) architecture, which is proficient in various natural language processing tasks, including summarization. This model is trained to generate summaries of input text based on a provided prompt or conditioning. It works in a text-to-text manner, meaning both the input and output are represented as text strings. Given a piece of text and a desired length or objective, the model generates a concise summary that captures the key information or main points from the input text. This capability makes it highly useful for automating the summarization process across different domains and applications


### Note
resources folder contain requierd files and module