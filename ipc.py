

import paho.mqtt.client as paho
import json
from threading import Thread
from event_treatment import *


class IPC(object):
    """docstring for IPC"""
    # event_treatment = None

    def __init__(self, event_treatment, username_CS, password_CS, host_CS, port_CS, username_ES, password_ES, host_ES, port_ES, topics):
        self.event_treatment = event_treatment

        # ========== Conexão com a propria borda ==========
        self.client_ES = paho.Client()
        self.client_ES.on_connect = self.on_connect_ES
        self.client_ES.on_message = self.on_message_ES
        self.client_ES.on_publish = self.on_publish_ES

        self.client_ES.username_pw_set(username=username_ES, password=password_ES)
        self.client_ES.connect(host=host_ES, port=port_ES)
        #==================================================
        # ============ Conexão com o Contexto =============
        self.client_CS = paho.Client()
        self.client_CS.on_connect = self.on_connect_CS
        self.client_CS.on_message = self.on_message_CS
        self.client_CS.on_publish = self.on_publish_CS

        self.client_CS.username_pw_set(username=username_CS, password=password_CS)
        self.client_CS.connect(host=host_CS, port=port_CS)
        #==================================================
        
        # Este tópico é utilizado para receber os dados dos gateways       
        self.add_subscribe_ES(topics)

        # Iniciaiza a conexão com a borda e contexto
        client_loop(self.client_ES).start()
        client_loop(self.client_CS).start()

    #==================================================
    # =============== Métodos da Borda ================ 
    def add_subscribe_ES(self, topics):
        for topic in topics:
            self.client_ES.subscribe(topic, 0)

    def on_connect_ES(self, client, userdata, flags, rc):
        print(rc)

    # Recebe a mensagem do broker e envia para o processamento de eventos para tratar a mensagem
    def on_message_ES(self, mosq, obj, msg):
        self.event_treatment.process_event(json.loads(msg.payload.decode("utf-8")),msg.topic)
        
    # Envia uma publicação para o Servidor de Contexto
    def on_publish_ES(self, topic, msg):
        # print(topic, msg)
        self.client_ES.publish(topic=topic, payload=msg, qos=0, retain=False)
    

    #==================================================
    # ============= Métodos da Contexto ===============
    def add_subscribe_CS(self, topico):
        self.client_CS.subscribe(topico, 0)

    def on_connect_CS(self, client, userdata, flags, rc):
        print(rc)

    # Recebe a mensagem do broker e envia para o processamento de eventos para tratar a mensagem
    def on_message_CS(self, mosq, obj, msg):
        # print(json.loads(msg.payload.decode("utf-8")))

        self.event_treatment.process_event(json.loads(msg.payload.decode("utf-8")))

    def on_publish_CS(self, topic, msg):
        self.client_CS.publish(topic=topic, payload=msg, qos=0, retain=False)
    #==================================================


class client_loop (Thread):
    def __init__(self,client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.loop_forever()
            