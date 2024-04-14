import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!"]
    ],
    [
        r"what is your name ?",
        ["You can call me ChatBot.", "I go by the name ChatBot."]
    ],
    [
        r"quit",
        ["Bye for now. Take care!", "Goodbye!"]
    ],
    
]

chatbot = Chat(pairs, reflections)

def chatbot_response(input_text):
    return chatbot.respond(input_text)

print("Welcome! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("ChatBot:", response)
    if user_input.lower() == "quit":
        break
