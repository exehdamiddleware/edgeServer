# from core.publisher_context import *
# from core.gathering import *
import threading
# import json
# from device import *
# from CRUD import *
from process_configuration import *

class Event_Treatment(object):
    # core = None

    #instância do objeto e inicia o escalonador
    def __init__(self):
        print("EVENT")
        # self.scheduler = scheduler
        #threading.Thread.__init__(self)
        self.process_configuration_db = Process_Configuration()
        self.process_scheduler_db = Process_Configuration()      

    def add_object_scheduler(self, object_scheduler):
        # print("ADD Scheduler")
        self.scheduler = object_scheduler

    def add_object_ipc(self, object_ipc):
        print("ADD IPC")
        self.ipc = object_ipc


    # Tipos de eventos:
    # - Agendamento de device
    # - Coleta ou atuação de um device
    # - Processamento de uma regra agendada
    # - Anúncio de recursos
    # - Recursos recebidos pelo GW
    # - Publicação
    # - Gathering - Action and collect

    def process_event(self, jsonObject):
        
        if jsonObject['type'] == "scheduler":
            print("SCHEDULER")
            self.scheduler.add_job(jsonObject)  
            # self.process_scheduler_db.scheduler(jsonObject)

        # Coleta ou atua um determinado device
        elif jsonObject['type'] == "device":
            print("Device event")
            device = Device(self.ipc, jsonObject['task']['uuid'])

        # Quando uma regra é chamada para processar os dados que estão no DB
        elif jsonObject['type'] == "rule":
            print("Rule event")

        # Recebe os dados de configuracao do GW, armazenando e enviando para o Servidor de Contexto
        elif jsonObject['type'] == "configuration":

            self.process_configuration_db.configuration(jsonObject)


        # Envia os dados para o Servidor de Contexto
        elif jsonObject['type'] == "collect":

            # Como diferenciar o tipo de publicação do GW e ES ?

            #from_gw_to_Edge_Server
            #receive_from_gw
            pass



        else:
            print(jsonObject)
            print("Unknown event")