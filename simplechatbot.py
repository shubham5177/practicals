# Simple chatbot

while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("Bot: Hello!")

    elif "how are you" in user:
        print("Bot: I am fine!")

    elif "name" in user:
        print("Bot: I am a chatbot.")

    elif "bye" in user:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I don't understand.")