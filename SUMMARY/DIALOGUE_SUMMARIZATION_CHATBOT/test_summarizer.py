#!/usr/bin/env python
# coding: utf-8

# In[3]:


from dialogue_summarizer import DialogueSummarizer

# Initialize the dialogue summarizer
summarizer = DialogueSummarizer("/Users/umeshkumarmalviya/Downloads/fine_tuned_dialogue_summary_csv_model_T5_60rows")

# Example usage
test_dialogue = "User: 'I placed an order two weeks ago, and it still hasn't arrived.' Bot: 'Can you provide your order number to check?'"
generated_summary = summarizer.generate_summary(test_dialogue)
print("Generated Summary:", generated_summary)


# In[ ]:




