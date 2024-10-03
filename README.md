ChatBot with JSON Intent Matching
Project Description
This is a simple command-line chatbot program built using Python. The bot matches user questions with predefined intents and responds accordingly. If the bot cannot find a matching question, it prompts the user to provide an answer and saves it for future interactions. The program uses a JSON file (intents.json) to store questions and answers, allowing the bot to "learn" from user interactions.

Features
1. Intelligent Matching: Uses the difflib.get_close_matches function to find the best match for a user’s question from a list of predefined questions.
2. Persistent Learning: The bot can learn new responses when it encounters an unknown question. It saves the newly learned question-answer pair into the intents.json file.
3. Customizable Intents: You can modify the intents.json file to add or update questions and answers.
Simple Command-Line Interface: Interacts with users directly from the terminal.

How It Works
1. The bot reads questions and answers from a intents.json file.
2. When the user inputs a question, the bot finds the closest match from its known questions using difflib.get_close_matches.
3. If a close match is found, the bot responds with the corresponding answer.
4. If no match is found, the bot asks the user for the correct answer and saves it for future use.
5. The conversation can be ended by typing quit.

Usage
1. Run the chatbot by executing the following command in the terminal:
   python chatbot.py
2. Start typing your questions. The bot will try to respond based on the predefined intents.
3. If the bot doesn't know the answer, it will ask you to teach it, and it will save the new question-answer pair for future interactions.
4. To exit the conversation, simply type quit.
