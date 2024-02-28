#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, AdamW

class DialogueSummarizer:
    def __init__(self, csv_file, num_epochs=3, model_name='t5-small'):
        self.csv_file = csv_file
        self.num_epochs = num_epochs
        self.model_name = model_name
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = None
        self.tokenizer = None
        self.train()

    def train(self):
        # Load CSV data and drop unnecessary columns
        data = pd.read_csv(self.csv_file)
        data = data.drop(columns=['id', 'topic'])
        # Consider only the first 40 rows of data
        data = data.head(40)
        # Extract input conversation and target summary
        train_data = [(row['dialogue'], row['summary']) for _, row in data.iterrows()]
        
        # Fine-tune the model
        tokenizer = T5Tokenizer.from_pretrained(self.model_name)
        model = T5ForConditionalGeneration.from_pretrained(self.model_name)
        model.to(self.device)
        model.train()

        # Prepare training data
        train_texts = [f"summarize: {conv}" for conv, _ in train_data]
        train_batch = tokenizer(train_texts, padding=True, truncation=True, return_tensors="pt")

        optimizer = AdamW(model.parameters(), lr=1e-4)

        for epoch in range(self.num_epochs):
            optimizer.zero_grad()
            outputs = model(input_ids=train_batch['input_ids'].to(self.device), labels=train_batch['input_ids'].to(self.device))
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            print(f"Epoch {epoch + 1}, Loss: {loss.item()}")

        self.model = model
        self.tokenizer = tokenizer

    def generate_summary(self, dialogue):
        if self.model is None:
            raise ValueError("Model has not been fine-tuned yet. Please call train() method first.")
        inputs = self.tokenizer.encode("summarize: " + dialogue, return_tensors="pt", max_length=512, truncation=True)
        inputs = inputs.to(self.device)
        with torch.no_grad():
            summary_ids = self.model.generate(inputs, num_beams=4, max_length=150, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

if __name__ == "__main__":
    # Initialize the dialogue summarizer and perform fine-tuning
    summarizer = DialogueSummarizer(csv_file="dialogue.csv")
    summarizer.train()

    # Example usage
    test_dialogues = ["#Person1#: Hi, Mr. Smith. I'm Doctor Hawkins. Why are you here today?\n#Person2#: I found it would be a good idea to get a check-up.\n#Person1#: Yes, well, you haven't had one for 5 years. You should have one every year.\n#Person2#: I know. I figure as long as there is nothing wrong, why go see the doctor?\n#Person1#: Well, the best way to avoid serious illnesses is to find out about them early. So try to come at least once a year for your own good.\n#Person2#: Ok.\n#Person1#: Let me see here. Your eyes and ears look fine. Take a deep breath, please. Do you smoke, Mr. Smith?\n#Person2#: Yes.\n#Person1#: Smoking is the leading cause of lung cancer and heart disease, you know. You really should quit.\n#Person2#: I've tried hundreds of times, but I just can't seem to kick the habit.\n#Person1#: Well, we have classes and some medications that might help. I'll give you more information before you leave.\n#Person2#: Ok, thanks doctor."]
    generated_summaries = [summarizer.generate_summary(dialogue) for dialogue in test_dialogues]
    for dialogue, summary in zip(test_dialogues, generated_summaries):
        print("Dialogue:", dialogue)
        print("Generated Summary:", summary)
        print()



# In[ ]:




