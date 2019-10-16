# from core.publisher_context import *
# from core.gathering import *
import threading
# import json
from device import *
# from CRUD import *
from process_configuration import *

class Event_Treatment(object):
    # core = None
    device = None
    ipc = None
    #instância do objeto e inicia o escalonador
    def __init__(self):
        print("EVENT")
        # self.scheduler = scheduler
        #threading.Thread.__init__(self)
        self.process_configuration_db = Process_Configuration()
        self.process_scheduler_db = Process_Configuration()   
         
    
    def add_object_scheduler(self, object_scheduler):
        # print("ADD Scheduler")
        # self.device = Device()
        # self.device.process("JUCA")
        self.scheduler = object_scheduler

    def add_object_ipc(self, object_ipc):
        print("ADD IPC")
        # self.device = Device()
        self.ipc = object_ipc
        self.device = Device_Process(self.ipc)

    # Tipos de eventos:
    # - Agendamento de device
    # - Coleta ou atuação de um device
    # - Processamento de uma regra agendada
    # - Anúncio de recursos
    # - Recursos recebidos pelo GW
    # - Publicação
    # - Gathering - Action and collect

    def process_event(self, jsonObject, topic=None):
        
        if jsonObject['type'] == "scheduler":
            print("SCHEDULER")
            self.scheduler.add_job(jsonObject)  
            self.process_scheduler_db.scheduler(jsonObject)

        # Coleta ou atua um determinado device
        elif jsonObject['type'] == "device":
            print("Device event")
            try:
                uuid_device = jsonObject['task']['uuid']
                self.device.process(uuid_device)
            except Exception as e:
                print(str(e))

        # Quando uma regra é chamada para processar os dados que estão no DB
        elif jsonObject['type'] == "rule":
            print("Rule event")

        # Recebe os dados de configuracao do GW, armazenando e enviando para o Servidor de Contexto
        elif jsonObject['type'] == "configuration":

            self.process_configuration_db.configuration(jsonObject)

        # Envia os dados para o Servidor de Contexto
        elif jsonObject['type'] == "collect":
            try:
                self.device.process(jsonObject, topic)
            except Exception as e:
                print(str(e))

        else:
            print(jsonObject)
            print("Unknown event")