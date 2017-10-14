"""
	This is the file that will hold all of the function calls
	The organization of this file will be classes that pertain
		to each API
	Naming should be done in camelCase and readable
"""

class Twilio(object):	
	def Twilio(self, sid, auth, number):
		from twilio.rest import Client
		self.client = Client(sid,auth)
		self.number = number;
	
	def sendText(toNum, message):
		self.client.api.account.messages.create(
			to=toNum,
			from_=number,
			body=message
		)

class Firebase(object):
	def Firebase(self, serviceKey, databaseURL, path):
		import firebase_admin
		from firebase_admin import credentials
		from firebase_admin import db

		cred = credentials.Certificate(serviceKey);

		firebase_admin.initialize_app(cred, {
			"databaseURL": databaseURL
		})

		self.ref = db.reference(path);

	def set(path, value):
		target = self.ref
		if(len(path) > 0)
			target = self.ref.child(path)

		parent = target.parent
		if parent != null:
			parent.set({target.key: value})

	def get(path, key):
		target = self.ref
		if(len(path) > 0)
			target = self.ref.child(path)
		return target.get()
		