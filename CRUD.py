
# import threading
#from models import Manufacturer, Gateway, Device, Context_Server, Persistance, Scheduler, Action_Rule, Rule
from models import *

class CRUD(object):
    def __init__(self):
        pass

    def create_manufacturer(self,name,address=None,phone=None,url=None,city=None,state=None,country=None):

        manufacturer = Manufacturer.create(name=name,address=address,phone=phone,url=url,city=city,state=state,country=country)
        
    def read_all_manufacturer(self):
            
        manufacturers = Manufacturer.select()
        return manufacturers

    def update_manufacturer(self, id):
        manufacturer = Manufacturer.get(Manufacturer.id==id)

        manufacturer.status = True
        manufacturer.save()

    def delete_manufacturer(self):
        pass

    #================================================================================================================

     
    def create_gateway(self,uuid,name,status=None,manufacturer_id=None):

        gateway = Gateway.create(uuid=uuid,name=name,status=status,manufacturer_id=manufacturer_id)
        
    def read_all_gateway(self):
            
        gateways = Gateway.select()
        return gateways

    def update_gateway(self, id):
        gateway = Gateway.get(Gateway.id==id)

        gateway.status = True
        gateway.save()

    def delete_gateway(self):
        pass
    #================================================================================================================



    def create_device(self,uuid,name=None,description=None,model=None,precision=None,unit=None,pin=None,driver=None,manufacturer_id=None,gateway_id=None):

        device = Device.create(uuid=uuid,name=name,description=description,model=model,precision=precision,unit=unit,pin=pin,driver=driver,manufacturer_id=manufacturer_id,gateway_id=gateway_id)
        
    def read_all_device(self):
            
        devices = Device.select()
        return devices

    def read_device(self, uuid):
        device = Device.get(Device.uuid == uuid)
        return device

    def update_device(self, id):
        device = Device.get(Device.id==id)

        device.status = True
        device.save()

    def delete_device(self):
        pass
    #================================================================================================================
     


    def create_context_server(self,uuid,name=None,ip=None,port=None,user=None,password=None):

        context_server = Context_Server.create(uuid=uuid,name=name,ip=ip,port=port,user=user,password=password)
        
    def read_all_context_server(self):
            
        context_server = Context_Server.select()
        return context_server

    def update_context_server(self, id):
        context_server = Context_Server.get(Context_Server.id==id)

        context_server.status = True
        context_server.save()

    def delete_context_server(self):
        pass
    #================================================================================================================



    def create_persistance(self,value,collect_date,publisher,device_uuid):

        persistance = Persistance.create(value=value,collect_date=collect_date,publisher=publisher,device_uuid=device_uuid)
        
    def read_all_persistance(self):
            
        persistance = Persistance.select()
        return persistance

    def update_persistance(self, id):
        persistance = Persistance.get(Persistance.id==id)

        persistance.status = True
        persistance.save()

    def delete_persistance(self):
        pass
    #================================================================================================================
    


    def create_scheduler(self,event,second,minute,hour,day,month,year,device_uuid):
        # print(event,second,minute,hour,day,month,year,device_uuid)

        scheduler = Scheduler.create(event=event,second=second,minute=minute,hour=hour,day=day,month=month,year=year,device_uuid=device_uuid)
        
    def read_all_scheduler(self):
        # print("=======================")
            
        scheduler = Scheduler.select()
        return scheduler

    def update_scheduler(self, id):
        scheduler = Scheduler.get(Scheduler.id==id)

        scheduler.status = True
        scheduler.save()

    def delete_scheduler(self):
        pass
    #================================================================================================================



    def create_action_rule(self,command):

        action_rule = Action_Rule.create(command=command)
        
    def read_all_action_rule(self):
            
        action_rule = Action_Rule.select()
        return action_rule

    def update_action_rule(self, id):
        action_rule = Action_Rule.get(Action_Rule.id==id)

        action_rule.status = True
        action_rule.save()

    def delete_action_rule(self):
        pass
    #================================================================================================================



    def create_rule(self,command,name,rule,action_rule_id,device_uuid):

        rule = Rule.create(command=command,name=name,rule=rule,action_rule_id=action_rule_id,device_uuid=device_uuid)
        
    def read_all_rule(self):
            
        rule = Rule.select()
        return rule

    def update_rule(self, id):
        rule = Rule.get(Rule.id==id)

        rule.status = True
        rule.save()

    def delete_rule(self):
        pass
    #================================================================================================================
    
# crud = CRUD()
# crud.create_manufacturer("Juca")
# crud.create_gateway("f8e3434f-af6e-4bc1-a23c-19dcfffddd5c","Teste",True,1)
# crud.create_device(uuid="7c58700d-86da-46a5-869a-2e1208460c25",manufacturer_id=1,gateway_id="f8e3434f-af6e-4bc1-a23c-19dcfffddd5c")
# crud.create_context_server("ab0a1146-25a4-43ea-8e7a-35e4833e6504")

