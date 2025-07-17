import datetime

# Intent keywords 
INTENTS = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "farewell": ["bye", "goodbye", "exit", "see you"],
    "status": ["how are you", "how's it going", "what's up"],
    "time": ["time", "clock", "current time"],
    "name": ["your name", "who are you"],
    "thanks": ["thank you", "thanks", "thx"],
    "suggest":["suggest exercises","suggest yoga"],
    "motivate":["motivate me"]
}

# Responses for above keywords
RESPONSES = {
    "greeting": ["Hi there!", "Hello!", "Hey! How can I assist you today?"],
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "status": ["I'm doing great, thanks!", "All systems operational!", "Feeling chatty!"],
    "time": [f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"],
    "name": ["I'm Dhundun, your friendly chatbot!", "You can call me Copilot."],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "suggest":["Good!,do Surya-Namaskar"],
    "motivate":["Kar Har Maidan a Fateh"]
   
}

# Memory for previous interactions
conversation_history = []

def detect_intent(user_input):
    user_input = user_input.lower()
    for intent, keywords in INTENTS.items():
        for keyword in keywords:
            if keyword in user_input:
                return intent
    return "unknown"

#defining chatbot function
def chatbot():
    print(" Hello! I'm Copilot, your enhanced chatbot. Type something...")

# Implementing While loop
    while True:
        user_input = input("You: ").strip()
        conversation_history.append(user_input)

        intent = detect_intent(user_input)

        if intent == "farewell":
            print(f"Bot: {RESPONSES[intent][0]}")
            break
        elif intent in RESPONSES:
            print(f"Bot: {RESPONSES[intent][0]}")
        else:
            print("Bot: I'm not sure I understand. Can you rephrase that?")

    print("\n Conversation Summary:")
    
    #implementing for loop
    for i, msg in enumerate(conversation_history, 1):
        print(f"{i}. {msg}")
        
#calling function
chatbot()