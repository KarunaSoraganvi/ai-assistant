# AI Assistant - Chatbot

An intelligent AI chatbot project built to demonstrate conversational AI capabilities.

## About
This project is created by **Karuna Soraganvi** as an introduction to AI and machine learning technologies.

## Features
- Natural language processing
- Context-aware responses
- Easy-to-extend architecture
- Simple command-line interface
- Conversation history tracking

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/KarunaSoraganvi/ai-assistant.git
cd ai-assistant
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Run the chatbot:
```bash
python main.py
```

### Example Interaction
```
==================================================
Welcome to Karuna's AI Assistant!
==================================================
Type 'exit' or 'quit' to end the conversation.

You: Hello
Karuna's AI Assistant: Hi there! What can I do for you?

You: What time is it?
Karuna's AI Assistant: The current time is 03:45 PM

You: What's today's date?
Karuna's AI Assistant: Today is Tuesday, May 20, 2026

You: bye
Karuna's AI Assistant: Goodbye! Have a great day!
```

## Project Structure
```
ai-assistant/
├── main.py              # Entry point
├── chatbot.py           # Core chatbot logic
├── requirements.txt     # Dependencies
├── README.md            # This file
└── .gitignore           # Git ignore rules
```

## Features Explained

### Greetings
The chatbot recognizes common greetings like "hello", "hi", "hey" and responds appropriately.

### Time & Date
Ask for the current time or date using natural language queries.

### Conversation History
The chatbot maintains a history of all conversations for future enhancements.

### Extensible Design
Easy to add new features and response patterns.

## Technologies
- Python 3.8+
- NLTK (Natural Language Processing)
- NumPy (Numerical computing)
- Requests (HTTP library)

## Future Enhancements
- Integration with APIs (weather, news, etc.)
- Machine learning model training
- Web interface (Flask/FastAPI)
- Multi-language support
- Sentiment analysis
- Advanced NLP with transformers

## Contributing
Feel free to fork this project and submit pull requests for any improvements!

## License
MIT

## Author
Karuna Soraganvi

---

**Happy Coding! 🚀**
