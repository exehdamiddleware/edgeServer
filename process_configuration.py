#!/usr/bin/env python
# -*- coding: utf-8 -*-

from CRUD import *

class Process_Configuration(object):
    # ------- Cadastro na borda ------- 
    # 1 - Cadastro do gateway
    # 2 - cadastro dos sensores

    # ------- Cadastro no SC ------- 
    # Relacionar o gateway a borda

    def __init__(self):
        self.crud = CRUD()
        
    def save_gateway(self, gateway):
        # Chama o método do CRUD para salvar os dados
        try:
            gateway_db = self.crud.read_gateway(uuid=gateway['uuid'])

            if gateway_db:
                try:
                    self.crud.update_gateway(uuid=gateway['uuid'],name=gateway['name'])
                    print("Update com sucesso do gateway")
                except Exception as e:
                    print("Erro ao realizar o update do gateway no DB")
                    print(str(e))

            else:
                try:
                    self.crud.create_gateway(uuid=gateway['uuid'],name=gateway['name'])
                    print("Cadastro com sucesso do gateway")
                except Exception as e:
                    print("Erro ao salvar os dados do gateway no DB")
                    print(str(e))
        except Exception as e:
                    print(str(e))
    
    def save_sensors(self, gateway, devices):
        # Chama o método do CRUD para salvar os dados
        try:
            for device in devices:
                device_db = self.crud.read_device(uuid=device['uuid'])

                if device_db:
                    try:
                        self.crud.update_device(uuid=device['uuid'],name=device['name'],pin=device['pin'],driver=device['driver'],gateway_id=gateway['uuid'])
                        print("Update com sucesso dos sensores")
                    except Exception as e:
                        print("Erro ao ealizar o update dos sensores no DB")
                        print(str(e))
                else:
                    try:
                        self.crud.create_device(uuid=device['uuid'],name=device['name'],pin=device['pin'],driver=device['driver'],gateway_id=gateway['uuid'])
                        print("Cadastro com sucesso dos sensores")
                    except Exception as e:
                        print("Erro ao salvar os dados dos sensores no DB")
                        print(str(e))
        except Exception as e:
                    print(str(e))

    def save_scheduler(self, conf):
        # Chama o método do CRUD para salvar os dados
        try:  # minute,hour,day,month,year,device_uuid
            self.crud.create_scheduler(event=conf['modo'],second=conf['second'],minute=conf['minute'],hour=conf['hour'],
                day=conf['day'],month=conf['month'],year=conf['year'],device_uuid=conf['task']['uuid'])
            print("Cadastro com sucesso do scheduler")
        except Exception as e:
            print("Erro ao salvar os dados do scheduler no DB")
            print(str(e))

    def get_gateway(self, uuid_sensor):
        try:
            data = self.crud.read_device(uuid_sensor)

            return data
        except Exception as e:
            print(str(e))

    def configuration(self, jsonObject):
        try:
            self.save_gateway(jsonObject['gateway'])

            self.save_sensors(jsonObject['gateway'],jsonObject['sensors'])
        except Exception as e:
            print(str(e))

    def scheduler(self, jsonObject):
        try:
            self.save_scheduler(jsonObject)
        except Exception as e:
            print(str(e))