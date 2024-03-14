import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

class DialogueSummarizer:
    def __init__(self, model_path):
        self.model = T5ForConditionalGeneration.from_pretrained(model_path)
        self.tokenizer = T5Tokenizer.from_pretrained(model_path)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
        self.model.eval()

    def generate_summary(self, dialogues):
        # Concatenate dialogues with a separator
        text = "".join(dialogues)
        
        # Adjust max_length dynamically based on the length of the input dialogues
        max_length = min(512, len(text) + 50)  # Adding extra padding
        
        # Tokenize and encode the text
        inputs = self.tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=max_length, truncation=True)
        inputs = inputs.to(self.device)
        
        # Generate summary
        with torch.no_grad():
            summary_ids = self.model.generate(inputs, num_beams=4, max_length=150, early_stopping=True)
        
        # Decode the summary and remove special tokens
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        return summary
