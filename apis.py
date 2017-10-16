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

'''
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
'''
		