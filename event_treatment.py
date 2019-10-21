#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
from device import *
from process_configuration import *

class Event_Treatment(object):
    device = None
    ipc = None
    #instância do objeto e inicia o escalonador
    def __init__(self, configuration):
        print("EVENT")
        # self.scheduler = scheduler
        #threading.Thread.__init__(self)
        self.process_configuration_db = Process_Configuration()
        self.process_scheduler_db = Process_Configuration()   

        self.configuration = configuration
         
    
    def add_object_scheduler(self, object_scheduler):
        self.scheduler = object_scheduler

    def add_object_ipc(self, object_ipc):
        print("ADD IPC")
        try:
            self.ipc = object_ipc
            self.device = Device_Process(self.ipc, self.process_configuration_db)
        except Exception as e:
            print(str(e))

    # Tipos de eventos:
    # - Agendamento de device
    # - Coleta ou atuação de um device
    # - Processamento de uma regra agendada
    # - Anúncio de recursos
    # - Recursos recebidos pelo GW
    # - Publicação
    # - Gathering - Action and collect

    def process_event(self, jsonObject, topic=None):

        try:
            if jsonObject['type'] == "scheduler":
                print("SCHEDULER")
                try:
                    self.scheduler.add_job(jsonObject)  
                    self.process_scheduler_db.scheduler(jsonObject)
                except Exception as e:
                    print(str(e))

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

                # Salva os dados de configuração do DB
                self.process_configuration_db.configuration(jsonObject)

                # Envia os dados de configuração para o Servidor de Contexto 
                try:
                    self.device.process_configuration(jsonObject, topic, self.configuration)
                except Exception as e:
                    print(str(e))

            # Envia os dados para o Servidor de Contexto
            elif jsonObject['type'] == "pub" or jsonObject['type'] == "collect":

                try:
                    self.device.process(jsonObject, topic)
                except Exception as e:
                    print(str(e))

            else:
                print(jsonObject)
                print("Unknown event")

        except Exception as e:
            print("Event Process")
            print(str(e))