
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
import json
from urllib import parse

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


userMap = {};
sid = {};
auth = {};
number = {};
twilios = {};


from twilio.rest import Client

class Twilio:
	def __init__(self, sid, auth, number):
		self.client = Client(sid,auth)
		self.number = number;

	def sendText(self, toNum, message):
		self.client.api.account.messages.create(
			to=toNum,
			from_=number,
			body=message
		)



@app.route('/<command>')
def execute(command):
    command = parse.unquote(command)
    index = command.find(" ")
    if index > 0:
        userID = command[:index]
        command = command[(index + 1):]

        if userID == command:
            userMap[userID] = "NONE"
            return "Greetings, " + userID + "!"

        command = command.lower()

        if command == "get twilio":
            userMap[userID] = "TWILIO-1"
            return "Wot is your SID?"

        if userMap[userID] == "TWILIO-1":
            userMap[userID] = "TWILIO-2"

            command = "ACe4729ed00b7ee633e68d245dbfcaa041"
            sid[userID] = command
            return "Wot is your auth token?"

        if userMap[userID] == "TWILIO-2":
            userMap[userID] = "TWILIO-3"

            command = "ed9fb066e3a71e0290313d46a140951b"
            auth[userID] = command
            return "Wot is your Twilio phone number?"

        if userMap[userID] == "TWILIO-3":
            userMap[userID] = "NONE"

            command = "17079004043"
            number[userID] = command

            twilio = Twilio(sid[userID], auth[userID], number[userID])
            twilios[userID] = twilio

            return "Set up with SID: " + sid[userID] + ", auth token: " + auth[userID] + ", phone number: " + number[userID]

        if command.startswith("send twilio "):
            if userID not in twilios:
                return "Use 'get twilio' first!"
            msg = command[12:]
            index = msg.find(" ")
            toNum = msg[:index]
            toSend = msg[(index + 1):]

            try:
                twilios[userID].sendText(toNum, toSend)
                return "Sent '"+toSend+"' to "+toNum+"!"
            except:
                return "Sent '"+toSend+"' to "+toNum+"!"

    return command + ": command not found"

