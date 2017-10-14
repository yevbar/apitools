"""
	This is the file that will hold all of the function calls
	The organization of this file will be classes that pertain
		to each API
	Naming should be done in camelCase and readable
"""

class Twilio(object):	
	def Twilio(self, sid, auth):
		from twilio.rest import Client
		self.client = Client(sid,auth)
	
	def sendText(fromNum, toNum, body_):
		self.client.api.account.messages.create(
			to=toNum,
			from_=fromNum,
			body=body_
		)
