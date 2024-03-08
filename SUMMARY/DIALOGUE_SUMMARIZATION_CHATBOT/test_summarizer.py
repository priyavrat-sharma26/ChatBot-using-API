
# In[3]:


from dialogue_summarizer import DialogueSummarizer

# Initialize the dialogue summarizer
#replace with the link to locally downloaded model
summarizer = DialogueSummarizer("C:/Users/saket.singh1/Downloads/fine_tuned_dialogue_summary_csv_model_T5_60rows-20240307T091913Z-001/fine_tuned_dialogue_summary_csv_model_T5_60rows")

# Example usage
test_dialogue = "User: 'I placed an order two weeks ago, and it still hasn't arrived.' Bot: 'give order number?'"
generated_summary = summarizer.generate_summary(test_dialogue)
print("Generated Summary:", generated_summary)


# In[ ]:




