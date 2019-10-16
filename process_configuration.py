from CRUD import *
# from DB.models import Manufacturer, Gateway, Device, Context_Server, Persistance, Scheduler, Action_Rule, Rule


class Process_Configuration(object):
    # ------- Cadastro na borda ------- 
    # 1 - Cadastro do gateway
    # 2 - cadastro dos sensores

    # ------- Cadastro no SC ------- 
    # Relacionar o gateway a borda

    def __init__(self):
        self.crud = CRUD()
        
    def save_gateway(self, gateway):
        # print(gateway)
        # Chama o método do CRUD para salvar os dados
        try: # create_gateway(self,uuid,name,status,manufacturer_id)
            self.crud.create_gateway(uuid=gateway['uuid'],name=gateway['name'])
            print("Cadastro com sucesso do gateway")
        except Exception as e:
            print("Erro ao salvar os dados do gateway no DB")
            print(str(e))
    
    def save_sensors(self, gateway, devices):
        # print(gateway, devices)
        # Chama o método do CRUD para salvar os dados
        try:
            for device in devices:
                #crud.create_device(uuid=device['uuid'],name=device['name'],description=device['description'],model=device['model'],precision=device[''],unit=device[''],pin=device['pin'],driver=device['driver'],manufacturer_id=device[''],gateway_id=device[''])
                self.crud.create_device(uuid=device['uuid'],name=device['name'],pin=device['pin'],driver=device['driver'],gateway_id=gateway['uuid'])
                print("Cadastro com sucesso dos sensores")
        except Exception as e:
            print("Erro ao salvar os dados dos sensores no DB")
            print(str(e))

    def save_scheduler(self, conf):
        # print(conf)
        # Chama o método do CRUD para salvar os dados
        try:  # minute,hour,day,month,year,device_uuid
            self.crud.create_scheduler(event=conf['modo'],second=conf['second'],minute=conf['minute'],hour=conf['hour'],
                day=conf['day'],month=conf['month'],year=conf['year'],device_uuid=conf['task']['uuid'])
            print("Cadastro com sucesso do scheduler")
        except Exception as e:
            print("Erro ao salvar os dados do scheduler no DB")
            print(str(e))


    def configuration(self, jsonObject):
        # print(jsonObject)
        self.save_gateway(jsonObject['gateway'])

        self.save_sensors(jsonObject['gateway'],jsonObject['sensors'])

    def scheduler(self, jsonObject):
        print("SCHEDULÇERRRRRRRR")
        self.save_scheduler(jsonObject)

        


