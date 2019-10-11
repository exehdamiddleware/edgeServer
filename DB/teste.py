from DB import *

db = DB()


db.insert_manufacturer(name="MF_1", address=None, phone=None,url=None,city=None,state=None,country=None)

db.insert_gateway(uuid="76677c4c-a2b0-4886-8035-73bcb2a922b8",name="GW_1",status=None,manufacturer_id=None)

db.insert_device(uuid="32c506aa-c101-47ae-aaf8-9c7ab82354e7",name="Sensor_1",description=None,model=None,precision=None,unit=None,pin=None,driver=None,manufacturer=None,gateway_id="76677c4c-a2b0-4886-8035-73bcb2a922b8")

db.insert_context_server(uuid="manufacturer",name="SC_1",ip="10",port="10",user="10",password="10")

db.insert_persistance(value=10,collect_date="12",publisher=1,device_uuid="32c506aa-c101-47ae-aaf8-9c7ab82354e7")

db.insert_scheduler(event="CRON",second="*",minute="*",hour="*",day="*",month="*",year="*",device_uuid="32c506aa-c101-47ae-aaf8-9c7ab82354e7")

# db.insert_action_rule(command="Teste")

db.insert_rule(name="Rule_1",rule="print('1')",action_rule_id=None,device_uuid="32c506aa-c101-47ae-aaf8-9c7ab82354e7")