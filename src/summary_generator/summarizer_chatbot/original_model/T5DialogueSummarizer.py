from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class T5DialogueSummarizer:

  def __init__(self, model_name="t5-base"):
    self.tokenizer = AutoTokenizer.from_pretrained(model_name)
    self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

  def summarize_dialogue(self, dialogue):
    dialogue_text = "\n".join(dialogue)
    inputs = self.tokenizer(dialogue_text, return_tensors="pt")
    summary_ids = self.model.generate(**inputs)
    summary_text = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary_text
