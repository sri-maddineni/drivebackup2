from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('SimpleBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Function to get a response from the chatbot
def get_bot_response(user_input):
    response = chatbot.get_response(user_input)
    return str(response)

# Chat loop
print("SimpleBot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("SimpleBot: Goodbye! Have a great day.")
        break
    response = get_bot_response(user_input)
    print("SimpleBot:", response)
