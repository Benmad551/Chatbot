import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"I'm sorry|My Fault|My bad",
        ["It's alright"]
    ],
    [
        r"What (.*) name",
        ["My name is Baxter"]
    ],
    [
        r"You are wrong|You're wrong",
        ["You are probably right"]
    ],
    [
        r"Whats wrong",
        ["Everything"]
    ],
    [
        r"No",
        ["Alright","Fine"]
    ],
    [
        r"(.*)",
        ["%1", "Can you clarify?", "I'm confused?"]
    ],
]

baxter_chatbot = Chat(pairs, reflections)

def baxter_chat():
    print("What is it now?")
    baxter_chatbot.converse()

def demo():
    baxter_chat()

if __name__ == "__main__":
    baxter_chat()
