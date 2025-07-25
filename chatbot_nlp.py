import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I'm your friendly chatbot, created using NLTK."]
    ],
    [
        r"how are you?",
        ["I'm doing great, thank you!"]
    ],
    [
        r"what can you do?",
        ["I can answer simple questions. Try saying 'hello', 'bye', or ask my name!"]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a nice day!"]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Try asking something else."]
    ]
]

# Start chatbot
def chat():
    print(" Chatbot: Hello! Type 'hello' to start.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    chat()