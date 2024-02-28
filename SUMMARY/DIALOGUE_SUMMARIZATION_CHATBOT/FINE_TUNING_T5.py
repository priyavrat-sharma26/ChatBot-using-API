#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, AdamW

# Loading CSV data 
data = pd.read_csv("dialogue.csv")
data = data.drop(columns=['id', 'topic'])

# Consider only the first 40 rows of data
data = data.head(40)

# Extract input conversation and target summary
train_data = [(row['dialogue'], row['summary']) for _, row in data.iterrows()]

# Fine-tune the model
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model.to(device)
model.train()

# Prepare training data
train_texts = [f"summarize: {conv}" for conv, _ in train_data]
train_summaries = [summary for _, summary in train_data]

train_batch = tokenizer(train_texts, padding=True, truncation=True, return_tensors="pt")

optimizer = AdamW(model.parameters(), lr=1e-4, no_deprecation_warning=True)

for epoch in range(3):  
    optimizer.zero_grad()
    outputs = model(input_ids=train_batch['input_ids'].to(device), labels=train_batch['input_ids'].to(device))
    loss = outputs.loss
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch + 1}, Loss: {loss.item()}")



model.save_pretrained("/Users/umeshkumarmalviya/Downloads/fine_tuned_dialogue_summary_csv_model_T5_60rows")
#you can save accordingly on local machine 


# In[3]:


output_path = "/Users/umeshkumarmalviya/Downloads/fine_tuned_dialogue_summary_csv_model_T5_60rows"
model.save_pretrained(output_path)
tokenizer.save_pretrained(output_path)


# In[ ]:




