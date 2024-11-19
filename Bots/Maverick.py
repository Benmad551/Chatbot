import nltk
from nltk.chat.util import Chat, reflections

"""
To Do:
Fill out more of the rules in Pairs

Maybe:
Add different chat bots? Ones that have different "Personalities" after figuring out how to dictate which to use

How does the Pairs work?
The first line with the r"string" is what the code looks for from user input
The line under that in its own [brackets] is the response the bot will give
If a input does not fall within one of the given "rules" the code outputs: None

Definitions:
 (.*) is just all the words inputted between the first part and the second part of the r"string"
 %1 takes the first part in parentheses and puts it in that place. It can go more than just one

Couldn't find a way to print text on a window using this method of a chatbot
"""

pairs = [
    # -------------------------------------------
    # Greetings
    # -------------------------------------------
    [
        r"Hi|hello|greetings",
        ["Hello", "Good Morning", "Hey!", ]
    ],
    [
        r"What's up?|Whats up?",
        ["Nothing much, how can I help you?", ]
    ],
    [
        r"My name is (.*)",
        ["Hello %1, what do you need help with?"]
    ],
    [
        r"How (.*) you",
        ["Good!"]
    ],
    # --------------------------------------
    # About
    # --------------------------------------
    [
        r"What (.*) name",
        ["My name is Maverick"]
    ],
    [
        r"Who is your (creator|builder)",
        ["ben is"]
    ],
    [
        r"What pip (.*)",
        ["Ben used nltk instead of chatterbot. nltk provided a simple chat bot function that worked on Python 3.12", ]
    ],
    [
        r"What (.*) Ben do",
        ["This line of code was the first line that Ben made after learning how to enter the rules", ]
    ],
    [
        r"(.*) (cool|nice) (.*) (today|now)",
        [" %1 %2 %3"]  # This is a test line to better understand how these work.
    ],
    [
        r"I need (.*)",
        ["I can help you with that!"]
    ],
    [
        r"No",
        ["Yes", "I say yes", ]
    ],

    [
        r"quit",
        ["I hope you enjoyed this version of the chatbot!", "I hope you liked this!", ]
    ],
]

maverick_chatbot = Chat(pairs, reflections)

def  maverick_chat():
    print("Welcome to Benjamin Madison's CSE 120 project using NLTK to create a chatbot. When you are done type 'quit'\n What would you like to talk about?")

    maverick_chatbot.converse()

def demo():
    maverick_chat()

# initiate the conversation
if __name__ == "__main__":
    maverick_chat()
