# from core.publisher_context import *
# from core.gathering import *
import threading
# import json
from device import *

class Event_Treatment(object):
    # core = None
    ipc = None
    scheduler = None
    #instância do objeto e inicia o escalonador
    def __init__(self, scheduler):
        self.scheduler = scheduler
        #threading.Thread.__init__(self)
        pass

    def add_object(self, object_ipc):
        self.ipc = object_ipc

    def process_event(self, jsonObject):
        # Tipos de eventos:
            # - Agendamento de device
            # - Coleta ou atuação de um device
            # - Processamento de uma regra agendada
            # - Anúncio de recursos
            # - Recursos recebidos pelo GW
            # - Publicação
            # - Gathering - Action and collect

        if jsonObject['type'] == "scheduler":
            print("Adicionando agendamento")
            self.scheduler.add_job(jsonObject)  

        # Coleta ou atua um determinado device
        elif jsonObject['type'] == "device":
            print("Device event")
            device = Device(self.ipc, jsonObject['task']['uuid'])

        # Quando uma regra é chamada para processar os dados que estão no DB
        elif jsonObject['type'] == "rule":
            print("Rule event")

        # Recebe os dados de configuracao do GW, armazenando e enviando para o Servidor de Contexto
        elif jsonObject['type'] == "configuration":
            # Como diferenciar o tipo configurações do GW e ES ?

            # Salvar os dados no DB

            # Envia os dados para o servidor de contexto   ---->>> Arrumar
            # self.ipc.on_publish("teste","mensagem")
            pass

        # Envia os dados para o Servidor de Contexto
        elif jsonObject['type'] == "collect":

            # Como diferenciar o tipo de publicação do GW e ES ?

            #from_gw_to_Edge_Server
            #receive_from_gw
            pass

        else:
            print(jsonObject)
            print("Unknown event")