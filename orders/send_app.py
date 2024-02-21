import environ
from flask import Flask, request
from send_sms import send_sms

app = Flask(__name__)
env = environ.Env()
#TODO: create incoming messages route

#TODO: create delivery reports route.

if __name__ == "__main__":
    #TODO: Call send message function
    
    app.run(debug=True, port =env('AFT_PORT'))