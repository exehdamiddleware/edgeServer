

from subscriber_2 import *

class IPC(object):
	"""docstring for IPC"""
	def __init__(self, username, password, host, port):
		# super(IPC, self).__init__()
		# self.arg = arg
		self.sub = Subscriber(username, password, host, port)
		# sub.add_subscribe('GW')
		self.sub.add_topic('GW')

	def	add_topic(self, topic):
		self.sub.add_subscribe(topic)