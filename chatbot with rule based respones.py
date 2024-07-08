import re

# Dictionary of predefined rules and responses
responses = {
    r'hello|hi|hey': 'Hello there! How can I help you today?',
    r'how are you\??': 'I am doing well, thank you!',
    r'bye|goodbye': 'Goodbye! Have a great day!',
    r'my name is (\w+)': 'Nice to meet you, {name}!',
    r'what is your age\??': 'I am a bot, so I don\'t have an age!',
    r'(\d+) (\+|\*) (\d+)': lambda match: str(eval(match.group(0))),
    r'(.*)': 'Sorry, I don\'t understand that. Can you please rephrase?'
}

def get_response(user_input):
    """ Retrieve an appropriate response based on the user input """
    for pattern, response in responses.items():
        match = re.match(pattern, user_input.strip(), re.IGNORECASE)
        if match:
            if callable(response):
                return response(match)
            elif '{name}' in response:
                return response.format(name=match.group(1))
            else:
                return response
    return None

def main():
    print("Bot: Hello! I'm your chatbot. You can start chatting or type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'bye':
            print("Bot:", get_response(user_input))
            break
        response = get_response(user_input)
        if response:
            print("Bot:", response)
        else:
            print("Bot: Sorry, I didn't get that. Can you please repeat?")

if __name__ == "__main__":
    main()
