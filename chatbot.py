import random

def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hi", "hello", "hey"]
    jokes = [
        "Why don’t programmers like nature? Too many bugs 😄",
        "Why did the computer go to the doctor? Because it caught a virus 🤖",
        "Why do Java developers wear glasses? Because they don’t C 👓"
    ]

    if any(greet in user_input for greet in greetings):
        return "Hello! 😊 How can I help you today?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😄"

    elif "your name" in user_input:
        return "I'm a simple chatbot built by Devuttyyy 🤖"

    elif "joke" in user_input:
        return random.choice(jokes)

    elif "bye" in user_input:
        return "Goodbye! Have a great day 🌟"

    else:
        return "Hmm 🤔 I’m not sure about that. Try asking something else!"
