from Maverick import maverick_chat
from Baxter import baxter_chat
from nltk.chat.util import Chat

bots = [
    (maverick_chat, "Maverick (First iteration)"),
    (baxter_chat, "Baxter (Second iteration)"),
]
# Found out the %d and %s are special ways in python to format strings.
# %d takes maverick_chat and turns it into an int
# %s takes the second part of the () and converts it into a string
def chats():
    print("What bot do you want to chat with?")
    count = len(bots)
    for i in range(count):
        print("  %d: %s" % (i + 1, bots[i][1]))
    while True:
        choice = input(f"\nPick a number between 1-{count}: ").strip()
        if choice.isdigit() and (int(choice) - 1) in range(count):
            break
        else:
            print("   Error: bad chatbot number")

    chatbot = bots[int(choice) - 1][0]
    chatbot()

if __name__ == "__main__":
    chats()
