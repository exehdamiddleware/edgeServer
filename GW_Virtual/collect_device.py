
class Collect_devide(object):
	subscriber = None
	"""docstring for ClassName"""
	def __init__(self):
		pass

	def add_object_subscriber(self, subscriber):
		self.subscriber = subscriber

	def collect_data(self, data):
		print(data)