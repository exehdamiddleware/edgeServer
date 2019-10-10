from table_db import *

import sqlite3

# conectando...

class DB(object):
	"""docstring for ClassName"""
	# conn = None
	# cursor = None
	def __init__(self):
		self.conn = sqlite3.connect('clientes.db')
		self.cursor = self.conn.cursor(self)
		Table(self.cursor)

	def insert_manufacturer(self, name, address=None, phone=None,url=None,city=None,state=None,country=None):
		# cursor = self.conn.cursor(self)

		sqlite_insert_query = """
		INSERT INTO 'manufacturer'
		('name','address','phone','url','city','state','country') 
		VALUES
		(?,?,?,?,?,?,?)"""

		record_to_insert = (name,address,phone,url,city,state,country)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into manufacturer")

	def read_all_manufacturer(self):
		sqlite_insert_query = """
		SELECT * FROM 'manufacturer';
		"""

		self.cursor.execute(sqlite_insert_query)
		
		return self.cursor.fetchall(self)

	def update_manufacturer(self):
		pass

	def delete_manufacturer(self):
		pass

	def insert_gateway(self,uuid,name=None,status=None,manufacturer_id=None):

		sqlite_insert_query = """
		INSERT INTO 'gateway'
		('uuid','name','status','manufacturer_id') 
		VALUES
		(?,?,?,?)"""

		record_to_insert = (uuid,name,status,manufacturer_id)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into gateway")

	def update_gateway(self):
		pass

	def delete_gateway(self):
		pass

	def insert_device(self, uuid,name=None,description=None,model=None,precision=None,unit=None,pin=None,driver=None,manufacturer_id=None,gateway_id=None):

		sqlite_insert_query = """
		INSERT INTO 'device'
		('uuid','name','description','model','precision','unit','pin','driver','manufacturer_id','gateway_id') 
		VALUES
		(?,?,?,?,?,?,?,?,?,?)"""

		record_to_insert = (uuid,name,description,model,precision,unit,pin,driver,manufacturer_id,gateway_id)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into device")

	def update_device(self):
		pass

	def delete_device(self):
		pass

	def insert_context_server(self,uuid,name=None,ip=None,port=None,user=None,password=None):

		sqlite_insert_query = """
		INSERT INTO 'context_server'
		('uuid','name','ip','port','user','password') 
		VALUES
		(?,?,?,?,?,?)"""

		record_to_insert = (uuid,name,ip,port,user,password)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into context server")

	def update_context_server(self):
		pass

	def delete_context_server(self):
		pass

	def insert_persistance(self,value,collect_date,publisher,device_uuid,context_server_id):

		sqlite_insert_query = """
		INSERT INTO 'persistance'
		('value','collect_date','publisher','device_uuid','context_server_id') 
		VALUES
		(?,?,?,?,?)"""

		record_to_insert = (value,collect_date,publisher,device_uuid,context_server_id)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into manufacturer")
		
	def update_persistance(self):
		pass

	def delete_persistance(self):
		pass

	def insert_scheduler(self,event,second,minute,hour,day,month,year,device_uuid):

		sqlite_insert_query = """
		INSERT INTO 'scheduler'
		('event','second','minute','hour','day','month','year','device_uuid') 
		VALUES
		(?,?,?,?,?,?,?)"""

		record_to_insert = (event,second,minute,hour,day,month,year,device_uuid)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into scheduler")

	def update_scheduler(self):
		pass

	def delete_scheduler(self):
		pass

	def insert_action_rule(self, command):

		sqlite_insert_query = """
		INSERT INTO 'action_rule'
		('command') 
		VALUES
		(?)"""

		record_to_insert = (command)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into action rule")

	def update_action_rule(self):
		pass

	def delete_action_rule(self):
		pass

	def insert_rule(self,name,rule,action_rule_id,device_uuid):

		sqlite_insert_query = """
		INSERT INTO 'rule'
		('name','rule','action_rule_id','device_uuid') 
		VALUES
		(?,?,?,?)"""

		record_to_insert = (name,rule,action_rule_id,device_uuid)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into rule")

	def update_rule(self):
		pass

	def delete_rule(self):
		pass
