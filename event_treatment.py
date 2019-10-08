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
        # print("EVENT")
        # print(jsonObject)

        # self.ipc.on_publish("teste", "Mensagem")
        # self.scheduler.add_job(jsonObject)


        # Tipos de eventos:
            # - Agendamento de device
            # - Agendamento de processamento
            # - Anúncio de recursos
            # - Processamento
            # - Publicação
            # - Gathering - Action and collect
        print(jsonObject)
        
        if jsonObject['type'] == "scheduler":
            print("Entrou")
            self.scheduler.add_job(jsonObject)            
        # Recebe os dados de configuracao do GW, armazenando e enviando para o Servidor de Contexto
        elif jsonObject['type'] == "conf":
            pass
        # # Recebe os dados de um determinado device, pode ser do sensor e atuador
        # elif jsonObject['type'] == "":
        #     pass
        # # Quando uma regra é chamada para processar os dados que estão no DB
        # elif jsonObject['type'] == "process":
        #     pass
        # # Envia os dados para o Servidor de Contexto
        # elif jsonObject['type'] == "publish":
        #     pass
        # # 
        # elif jsonObject['type'] == "device":
        #     pass
        # else:
        #     print("Nenhum tipo de evento em operação")


        # if jsonObject['event'] == "proceeding":
        #     print('Proceeding')
        #         #event = Proceeding(self.request_API_to_DB)

        # elif jsonObject['event'] == "publisher":
        #     #print('Publisher')
        #     event = Publisher(self.core)
        #     # print(dir(Publisher))
        #     event.publish_to_rules(jsonObject)

        # elif jsonObject['event'] == "gathering":
        #     event = Gathering(self.core)
        #     return_parameters = event.processamento(jsonObject) # 1 em referencia ao sensor 1
        #     return return_parameters
        # else:
        #     print("Nenhum do casos no TRATAMENTO EVENTO 2")