#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import datetime

class Device_Process(object):
    ipc = None

    def __init__(self, ipc, process_configuration_db):
        self.ipc = ipc
        self.process_configuration_db = process_configuration_db

    # Realiza uma busca no DB realacionando o sensor com o GW em busca do uuid
    # Topico de publisher GW_ + (uuid do GW)
    def process(self, data, topic=None):
        
        # Dado é enviado para o CS com o topico recebido
        try:  
            if topic:
                
                date_now = datetime.datetime.now()
                date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
      
                data["date"] = date_str

                data = json.dumps(data)

                self.ipc.on_publish_CS(topic, data)

            # É feita uma "requisição" para um determinado device
            else:
                #Acesso ao DB em busca do uuid do GW
                sensor = self.process_configuration_db.get_gateway(data)

                # Topic de publicação do gateway e mensagem a ser enviada
                topic = "GW_" + str(sensor.gateway_id)
                print(topic)
                msg = {'uuid': data}
                msg = json.dumps(msg)

                # Envia mensagem para o topico especifico, enviando para GW em questão
                self.ipc.on_publish_ES(topic, msg)
        except Exception as e:
            print(str(e))

    def process_configuration(self, data, topic, configuration):

        try:
            data["edge"] = {}
            data["edge"]["uuid"] = configuration['edge_server']['uuid']
            #data["edge"]["username"] = configuration['broker_mqtt_ES']['user']
            #data["edge"]["password"] = configuration['broker_mqtt_CS']['password']
            #data["edge"]["ip"] = configuration['broker_mqtt_CS']['ip']
            #data["edge"]["port"] = configuration['broker_mqtt_CS']['port']
            #data["edge"]["name"] = configuration['edge_server']['name']

            msg = json.dumps(data)

            self.ipc.on_publish_CS(topic, msg)
        except Exception as e:
            print(str(e))
