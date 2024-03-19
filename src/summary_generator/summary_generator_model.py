from transformers import T5ForConditionalGeneration, T5Tokenizer

class DialogueSummarizer:
    def __init__(self, model_path):
        self.model = T5ForConditionalGeneration.from_pretrained(model_path)
        self.tokenizer = T5Tokenizer.from_pretrained(model_path)
        self.model.eval()

    def generate_summary(self, dialogue):
        text = " ".join(dialogue)
        inputs = self.tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = self.model.generate(inputs, num_beams=4, max_length=150, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

