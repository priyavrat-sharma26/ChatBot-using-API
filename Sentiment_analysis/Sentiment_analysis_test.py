#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Sentiment_analysis import SentimentAnalysis
classifier = SentimentAnalysis()
classifier.give_sentiment("I am so happy today")
conversation = [
    {'role': 'User', 'message': "Hello, I've been experiencing some issues with my internet connection. It's been quite slow for the past couple of days."},
    {'role': 'Customer Care Agent', 'message': "Hi there! I'm sorry to hear that you're facing issues with your internet. I'll do my best to help you out. Can you please provide me with your account number or the phone number associated with your account?"},
    {'role': 'User', 'message': "Sure, my account number is 123456789."},
    {'role': 'Customer Care Agent', 'message': "Thank you for providing that information. I appreciate it. Let me check the status of your connection. It seems there might be some technical difficulties. Have you noticed any specific times when the internet is slower than usual?"},
    {'role': 'User', 'message': "It's been consistently slow, but it does seem worse during peak hours in the evenings."},
    {'role': 'Customer Care Agent', 'message': "I see. Thank you for letting me know. I'll run a diagnostic on your connection to see if there are any issues on our end. In the meantime, have you tried restarting your router recently? It might help improve the speed."},
    {'role': 'User', 'message': "Yes, I've already tried restarting the router a couple of times, but it hasn't made much of a difference."},
    {'role': 'Customer Care Agent', 'message': "Thank you for trying that. I appreciate your cooperation. While I'm checking on the diagnostics, could you also confirm if the issue persists on multiple devices? This will help us narrow down the potential causes."},
    {'role': 'User', 'message': "Yes, I've noticed the slow speed on both my laptop and my smartphone."},
    {'role': 'Customer Care Agent', 'message': "Got it. Thank you for providing that information. It helps us identify the scope of the issue. It may take a few moments for the diagnostics to complete. In the meantime, is there anything else you'd like to share about the problem?"},
    {'role': 'User', 'message': "Not really, just hoping we can get it resolved soon. It's been quite inconvenient."},
    {'role': 'Customer Care Agent', 'message': "I completely understand, and I apologize for the inconvenience. We'll do our best to address the issue promptly. While we wait for the diagnostics, is there anything else you would like assistance with or any other questions you may have?"},
    {'role': 'User', 'message': "No, that's it for now. I appreciate your help."},
    {'role': 'Customer Care Agent', 'message': "You're welcome! I appreciate your patience. I'll continue to investigate the issue and will update you as soon as I have more information. If you have any further questions or concerns, feel free to reach out. Thank you for choosing our service, and have a great day!"}
]
for msg in conversation:
    if msg["role"] == 'User':
        print(msg["message"]+" | ",classifier.give_sentiment(msg["message"]))

