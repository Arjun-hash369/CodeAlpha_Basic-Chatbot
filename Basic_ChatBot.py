# Basic Chatbot
# Created by Arjun Muluk
# Internship Task 3

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    elif user_input == "your name":
        return "I'm a simple chatbot created in Python."
    else:
        return "Sorry, I don't understand that."

def main():
    print("🤖 Chatbot Started (type 'bye' to exit)")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() == "bye":
            break

# Run the chatbot
main()