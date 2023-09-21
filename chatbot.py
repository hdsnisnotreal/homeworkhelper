import random

# Define a dictionary of predefined questions and answers
homework_questions = {
    "math": ["What math problem do you need help with?", "Sure, I can help with math. What's your question?"],
    "science": ["Ask me a science question, and I'll do my best to help.", "Science is interesting! What's your question?"],
    "history": ["I can assist with history questions. What's on your mind?", "History, you say? Ask away!"],
    "english": ["Need help with an English assignment? Tell me more.", "I'm here to help with English. What's your question?"],
    "default": ["I'm sorry, I can't help with that. Please ask a different question.", "I don't have information on that topic."]
}

# Function to generate a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    
    if "math" in user_input:
        return random.choice(homework_questions["math"])
    elif "science" in user_input:
        return random.choice(homework_questions["science"])
    elif "history" in user_input:
        return random.choice(homework_questions["history"])
    elif "english" in user_input:
        return random.choice(homework_questions["english"])
    else:
        return random.choice(homework_questions["default"])

# Main loop for the chatbot
print("Hello! I'm your homework help chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye! Have a great day.")
        break
    else:
        response = get_response(user_input)
        print("Chatbot:", response)
