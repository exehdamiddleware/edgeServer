# from core.publisher_context import *
# from core.gathering import *
# import threading
# import json

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
            # - Agendamento de processamento
            # - Anúncio de recursos
            # - Publicação
            # - Gathering - Action and collect

        if jsonObject['type'] == "scheduler":
            print("Add Agendamento")
            self.scheduler.add_job(jsonObject)  
        # Quando uma regra é chamada para processar os dados que estão no DB
        elif jsonObject['type'] == "rule":
            print("Rule event")
        # Recebe os dados de configuracao do GW, armazenando e enviando para o Servidor de Contexto
        elif jsonObject['type'] == "conf":
            # Salvar os dados no DB
            self.ipc.on_publish("teste","mensagem")
        # Envia os dados para o Servidor de Contexto
        elif jsonObject['type'] == "publish":
            print("Send message to CS")
        # Recebe os dados de um determinado device, pode ser do sensor e atuador
        elif jsonObject['type'] == "device":
            print("Device event")
        else:
            print("Unknown event")