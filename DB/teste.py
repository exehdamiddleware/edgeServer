from DB import *

db = DB()
db.insert_manufacturer(self, name, address=None, phone=None,url=None,city=None,state=None,country=None)

db.insert_gateway(self,uuid,name=None,status=None,manufacturer_id=None)

db.insert_device(self, uuid,name=None,description=None,model=None,precision=None,unit=None,pin=None,driver=None,manufacturer_id=None,gateway_id=None)

db.insert_context_server(self,uuid,name=None,ip=None,port=None,user=None,password=None)

db.insert_persistance(self,value,collect_date,publisher,device_uuid,context_server_id)

db.insert_scheduler(self,event,second,minute,hour,day,month,year,device_uuid)

db.insert_action_rule(self, command):

db.insert_rule(self,name,rule,action_rule_id,device_uuid)