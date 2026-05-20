"""
AI Assistant Chatbot Module
Author: Karuna Soraganvi
"""

import datetime
import random


class AIAssistant:
    """Simple AI Assistant for conversational chatbot"""
    
    def __init__(self, name="AI Assistant"):
        self.name = name
        self.conversation_history = []
        self.greetings = [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Greetings! How are you doing?",
            "Welcome! How may I assist you?"
        ]
        self.farewells = [
            "Goodbye! Have a great day!",
            "See you later!",
            "Thanks for chatting! Bye!",
            "Take care!"
        ]
    
    def get_response(self, user_input):
        """Generate response based on user input"""
        user_input_lower = user_input.lower()
        
        # Check for greetings
        if any(word in user_input_lower for word in ["hello", "hi", "hey"]):
            return random.choice(self.greetings)
        
        # Check for farewell
        if any(word in user_input_lower for word in ["bye", "goodbye", "exit", "quit"]):
            return random.choice(self.farewells)
        
        # Check for time query
        if any(word in user_input_lower for word in ["time", "what time", "current time"]):
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}"
        
        # Check for date query
        if any(word in user_input_lower for word in ["date", "today", "what day"]):
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            return f"Today is {current_date}"
        
        # Default response
        return f"That's interesting! I understand you said: '{user_input}'. Tell me more!"
    
    def chat(self):
        """Main chat loop"""
        print(f"\n{'='*50}")
        print(f"Welcome to {self.name}!")
        print(f"{'='*50}")
        print("Type 'exit' or 'quit' to end the conversation.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Check for exit commands
                if user_input.lower() in ["exit", "quit", "bye"]:
                    response = random.choice(self.farewells)
                    print(f"{self.name}: {response}\n")
                    break
                
                # Get and display response
                response = self.get_response(user_input)
                print(f"{self.name}: {response}\n")
                
                # Store in history
                self.conversation_history.append({
                    "user": user_input,
                    "assistant": response
                })
                
            except KeyboardInterrupt:
                print(f"\n{self.name}: Goodbye!\n")
                break
            except Exception as e:
                print(f"Error: {e}\n")
