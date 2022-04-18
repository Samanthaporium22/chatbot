#chatbot nltk modules
from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections
from staff_training import responsepair as pairs
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response("Hello, World!")

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("localhost", 5000, application)
    
app = Flask(__name__)

@app.route('/')
def firstChatBot():
    print ("Hi, I am Nerd Bot build with the NLTK module")
    print ("I can assist you to find information for Staff Resource Officers")
    print ("Type help if you get stuck or quit to exit")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()
if __name__ == '__main__':
    firstChatBot()

    
