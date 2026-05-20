#!/usr/bin/env python3
"""
AI Assistant - Main Entry Point
Author: Karuna Soraganvi
"""

from chatbot import AIAssistant


def main():
    """Main function to run the AI Assistant"""
    assistant = AIAssistant(name="Karuna's AI Assistant")
    assistant.chat()


if __name__ == "__main__":
    main()
