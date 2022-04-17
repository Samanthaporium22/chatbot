#chatbot nltk modules
from nltk.chat.util import Chat, reflections
from staff_training import responsepair as pairs

# ngrok authentication token:
# 27v4lpVa7QYDAJ0KiqaUUbK6ANc_4aaq5LyDNFCcPRG7ozqhz


def firstChatBot():
    print ("Hi, I am Nerd Bot build with the NLTK module")
    print ("I can assist you to find information for Staff Resource Officers")
    print ("Type help if you get stuck or quit to exit")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()
if __name__ == '__main__':
    firstChatBot()
    
