

import paho.mqtt.client as paho
import json
from threading import Thread
from event_treatment import *


class IPC(object):
    """docstring for IPC"""
    event_treatment = None

    def __init__(self, event_treatment, username, password, host, port):
        self.event_treatment = event_treatment

        self.client = paho.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish

        self.client.username_pw_set(username=username, password=password)
        self.client.connect(host=host, port=port)
        self.add_subscribe("GW")
        client_loop(self.client).start()

    def add_subscribe(self, topico):
        self.client.subscribe(topico, 0)

    def on_connect(self, client, userdata, flags, rc):
        print(rc)

    # Recebe a mensagem do broker e envia para o processamento de eventos para tratar a mensagem
    def on_message(self, mosq, obj, msg):
        self.event_treatment.process_event(json.loads(msg.payload.decode("utf-8")))
        
    # def on_publish(self, mosq, obj, mid):
    # Envia uma publicação para o Servidor de Contexto
    def on_publish(self, topic, msg):
        self.client.publish(topic=topic, payload=msg, qos=0, retain=False)
        

class client_loop (Thread):
    def __init__(self,client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.loop_forever()
            