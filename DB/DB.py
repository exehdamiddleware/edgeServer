from table_db import *

import sqlite3

# conectando...

class DB(object):
	"""docstring for ClassName"""
	# conn = None
	# cursor = None
	def __init__(self):
		pass
		self.conn = sqlite3.connect('clientes.db')
		self.cursor = self.conn.cursor()
		Table(self.cursor)

	#====================================================================================================================

	def insert_manufacturer(self,id_generic,name,address=None,phone=None,url=None,city=None,state=None,country=None):
		# cursor = self.conn.cursor(self)

		sqlite_insert_query = """
		INSERT INTO 'manufacturer'
		('id','name','address','phone','url','city','state','country') 
		VALUES
		(?,?,?,?,?,?,?,?)"""

		record_to_insert = (id_generic,name,address,phone,url,city,state,country)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into manufacturer")

	def read_all_manufacturer(self):
		sqlite_insert_query = """
		SELECT * FROM 'manufacturer';
		"""

		self.cursor.execute(sqlite_insert_query)
		
		return self.cursor.fetchall()

	def update_manufacturer(self,id_generic,name,address=None,phone=None,url=None,city=None,state=None,country=None):
		pass

	def delete_manufacturer(self, id_generic):
		try:
			sqlite_insert_query = """
			SELECT * FROM 'manufacturer'
			WHERE id = ?
			"""

			record_to_insert = (id_generic,)

			self.cursor.execute(sqlite_insert_query, record_to_insert)

			self.conn.commit()
		except:
			print("Unable to delete manufacturer")

	#====================================================================================================================

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

	def read_all_gateway(self):
		sqlite_insert_query = """
		SELECT * FROM 'gateway';
		"""

		self.cursor.execute(sqlite_insert_query)
		
		return self.cursor.fetchall()

	def update_gateway(self,uuid,name=None,status=None,manufacturer_id=None):
		pass

	def delete_gateway(self, uuid):
		pass

	#====================================================================================================================

	def insert_device(self,uuid,name=None,description=None,model=None,precision=None,unit=None,pin=None,driver=None,manufacturer=None,gateway_id=None):

		sqlite_insert_query = """
		INSERT INTO 'device'
		('uuid','name','description','model','precision','unit','pin','driver','manufacturer','gateway_id') 
		VALUES
		(?,?,?,?,?,?,?,?,?,?)"""

		record_to_insert = (uuid,name,description,model,precision,unit,pin,driver,manufacturer,gateway_id)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into device")

	def read_all_device(self):
		sqlite_insert_query = """
		SELECT * FROM 'device';
		"""

		self.cursor.execute(sqlite_insert_query)
		
		return self.cursor.fetchall()

	def update_device(self, uuid,name=None,description=None,model=None,precision=None,unit=None,pin=None,driver=None,manufacturer=None,gateway_id=None):
		pass

	def delete_device(self, uuid):
		pass

	#====================================================================================================================

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

	def read_all_context_server(self):
		sqlite_insert_query = """
		SELECT * FROM 'context_server';
		"""

		self.cursor.execute(sqlite_insert_query)
		
		return self.cursor.fetchall()

	def update_context_server(self,uuid,name=None,ip=None,port=None,user=None,password=None):
		pass

	def delete_context_server(self,uuid):
		pass

	#====================================================================================================================

	def insert_persistance(self,id_generic,value,collect_date,publisher,device_uuid):

		sqlite_insert_query = """
		INSERT INTO 'persistance'
		('id','value','collect_date','publisher','device_uuid') 
		VALUES
		(?,?,?,?,?)"""

		record_to_insert = (id_generic,value,collect_date,publisher,device_uuid)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into manufacturer")

	def read_all_persistance(self):
		sqlite_insert_query = """
		SELECT * FROM 'persistance';
		"""

		self.cursor.execute(sqlite_insert_query)
		
		return self.cursor.fetchall()
		
	def update_persistance(self,value,collect_date,publisher,device_uuid):
		pass

	def delete_persistance(self,id):
		pass

	#====================================================================================================================

	def insert_scheduler(self,id_generic,event,second,minute,hour,day,month,year,device_uuid):

		sqlite_insert_query = """
		INSERT INTO 'scheduler'
		('id','event','second','minute','hour','day','month','year','device_uuid') 
		VALUES
		(?,?,?,?,?,?,?,?,?)"""

		record_to_insert = (event,second,minute,hour,day,month,year,device_uuid)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into scheduler")

	def read_all_scheduler(self):
		sqlite_insert_query = """
		SELECT * FROM 'scheduler';
		"""

		self.cursor.execute(sqlite_insert_query)
		
		return self.cursor.fetchall()

	# def update_scheduler(self,id_generic,event=None,second=None,minute=None,hour=None,day=None,month=None,year=None,device_uuid):
		# pass

	def delete_scheduler(self,id_generic):
		pass

	#====================================================================================================================

	def insert_action_rule(self, id_generic,command):

		sqlite_insert_query = """
		INSERT INTO 'action_rule'
		('id','command') 
		VALUES
		(?,?)"""

		record_to_insert = (command)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into action rule")

	def read_all_action_rule(self):
		sqlite_insert_query = """
		SELECT * FROM 'action_rule';
		"""

		self.cursor.execute(sqlite_insert_query)
		
		return self.cursor.fetchall()

	def update_action_rule(self,id_generic,command):
		pass

	def delete_action_rule(self,id_generic):
		pass

	#====================================================================================================================

	def insert_rule(self,id_generic,name,rule,action_rule_id,device_uuid):

		sqlite_insert_query = """
		INSERT INTO 'rule'
		('id','name','rule','action_rule_id','device_uuid') 
		VALUES
		(?,?,?,?,?)"""

		record_to_insert = (id_generic,name,rule,action_rule_id,device_uuid)

		self.cursor.execute(sqlite_insert_query, record_to_insert)
		self.conn.commit()
		print("Record inserted successfully into rule")

	def read_all_rule(self):
		sqlite_insert_query = """
		SELECT * FROM 'rule';
		"""

		self.cursor.execute(sqlite_insert_query)
		
		return self.cursor.fetchall()

	def update_rule(self,id_generic):
		pass

	def delete_rule(self,id_generic):
		pass
