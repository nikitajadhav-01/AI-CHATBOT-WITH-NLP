

import random
import string
from nltk.stem import WordNetLemmatizer
import nltk


try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')


lemmatizer = WordNetLemmatizer()

intents = {
    'greeting': {
        'patterns': ['hi', 'hello', 'hey', 'hii', 'good morning', 'good evening'],
        'responses': ['Hello!', 'Hi there!', 'Greetings!', 'How can I help you today?']
    },
    'goodbye': {
        'patterns': ['bye', 'see you', 'goodbye', 'quit', 'exit'],
        'responses': ['Goodbye!', 'See you later!', 'Have a nice day!']
    },
    'thanks': {
        'patterns': ['thanks', 'thank you', 'thx'],
        'responses': ['You’re welcome!', 'No problem!', 'Glad to help!']
    },
    'name': {
        'patterns': ['what is your name', 'who are you'],
        'responses': ['I am a simple AI chatbot created with Python and NLTK.']
    },
    'help': {
        'patterns': ['help', 'can you help me', 'what can you do'],
        'responses': ['I can answer basic questions and greet you. Try saying "hi"!']
    }
}



def preprocess(sentence):
    """
    Tokenize and lemmatize the input sentence.
    Using simple split() to avoid NLTK punkt issues.
    """
    tokens = sentence.lower().split()
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in string.punctuation]
    return tokens

def check_intent(user_input):
    """
    Match user input with intents and return a response.
    """
    user_tokens = preprocess(user_input)

    for intent, data in intents.items():
        for pattern in data['patterns']:
            pattern_tokens = preprocess(pattern)
            if all(word in user_tokens for word in pattern_tokens):
                return random.choice(data['responses'])

    return "Sorry, I didn't understand that. Could you rephrase?"

def chatbot():
    """
    Main chatbot loop.
    """
    print("🤖 Chatbot is ready! (type 'quit' or 'exit' to leave)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Chatbot: Goodbye! 👋")
            break
        response = check_intent(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chatbot()
