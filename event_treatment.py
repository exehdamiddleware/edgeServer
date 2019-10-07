# from core.publisher_context import *
# from core.gathering import *
# import threading
# import json

class Event_Treatment(object):
    # core = None

    #instância do objeto e inicia o escalonador
    def __init__(self, ipc):
        #threading.Thread.__init__(self)
        self.ipc = ipc
        pass

    def process_event(self, jsonObject):
        # print("EVENT")
        # print(jsonObject)

        # Tipos de eventos:
            # - Anúncio de recursos
            # - Recebe uma coleta de dados
            # - Processamento
            # - Publicação
            # - Gathering - Action

        # Recebe os dados de configuracao do GW, armazenando e enviando para o Servidor de Contexto
        if jsonObject['type'] == "configuration":
            pass
        # Recebe os dados de um determinado device, pode ser do sensor e atuador
        elif jsonObject['type'] == "":
            pass
        # Quando uma regra é chamada para processar os dados que estão no DB
        elif jsonObject['type'] == "process":
            pass
        # Envia os dados para o Servidor de Contexto
        elif jsonObject['type'] == "publish"::
            pass
        # 
        elif jsonObject['type'] == "device"::
            pass
        else:
            print("Nenhum tipo de evento em operação")


        # Tipos de eventos:
            # - Anúncio de recursos
            # - Recebe uma coleta de dados
            # - Processamento
            # - Publicação
            # - Gathering - Action


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