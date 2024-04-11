import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class NextSentencePrediction():
    def __init__(self, model_path):
        self.model = GPT2LMHeadModel.from_pretrained(model_path)
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    def generate_agent_responses(self,customer_input):
    # Example dialogue for context
        example_customer_query = "Customer: What is the status of my order?"
        example_agent_response = "Agent: Your order is being processed and will be shipped soon."
        
        # Combine the example dialogue with the actual customer input
        input_text = f"{example_customer_query} {example_agent_response} {customer_input} Agent:"
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt')
        attention_mask = torch.ones(input_ids.shape)

        # Generate a response from the model
        outputs = self.model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_length=150,  # Adjusted to ensure complete response
            pad_token_id=self.tokenizer.eos_token_id,
            temperature=0.4,
            top_k=50,   #50
            top_p=0.95, #0.95
            repetition_penalty=1.2,
            num_beams=1,  # Using greedy search
            early_stopping=True,
            num_return_sequences=1,
            do_sample=True  # Enable sampling for more diverse responses
        )

        # Decode and extract the agent's response
        text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        agent_response = text.split(customer_input)[-1].split('Agent:')[1].strip()
        return agent_response
