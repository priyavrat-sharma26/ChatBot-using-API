from transformers import T5ForConditionalGeneration, T5Tokenizer

class DialogueSummarizer:
    def __init__(self, model_path):
        self.model = T5ForConditionalGeneration.from_pretrained(model_path)
        self.tokenizer = T5Tokenizer.from_pretrained(model_path)
        self.model.eval()

    def generate_summary(self, dialogue, max_length=300, num_beams=4, no_repeat_ngram_size=2): #max_length=150
        text = ""
        last_speaker = None
        for line in dialogue:
            if ": " in line:
                current_speaker, utterance = line.split(": ", 1)
                if last_speaker and current_speaker != last_speaker:
                    text += "\n"
                text += current_speaker + ": " + utterance
                last_speaker = current_speaker
            else:
                text += " " + line  # Append lines without a speaker to the previous line.
        example_dialogue = "Agent: How can I assist you today? User: I need to change my address. Agent: Sure, I can help with that."
        example_summary = "The user needed to change their address, and the agent assisted with the process."

        prompt = (f"Example dialogue: '{example_dialogue}' Example summary: '{example_summary}' "
                  f"Summarize the key points and resolutions from the following customer service dialogue: {text}")
        #prompt = "Summarize the key points and resolutions from the following customer service dialogue: " + text

        # Ensure the entire dialogue is considered without truncation
        encoding = self.tokenizer.encode_plus(prompt, return_tensors="pt", max_length=1024, truncation=True)
        input_ids, attention_masks = encoding["input_ids"], encoding["attention_mask"]

        # Generate the summary
        summary_ids = self.model.generate(input_ids, attention_mask=attention_masks, num_beams=num_beams,
                                          max_length=max_length, early_stopping=True, no_repeat_ngram_size=no_repeat_ngram_size)

        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
