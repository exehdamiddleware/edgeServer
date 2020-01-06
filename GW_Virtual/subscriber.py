#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
import paho.mqtt.client as paho
import random
import json
import datetime

class Subscriber(object):
    
    def __init__(self,device,username_ES,password_ES,host_ES,port_ES,topic_ES,sensors,gateway):

        self.client = paho.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.username_pw_set(username=username_ES, password=password_ES)

        self.client.connect(host_ES, port_ES)
        self.add_subscribe('GW_'+gateway['uuid'])

        self.sensors = sensors
        self.gateway = gateway
        self.topic_pub = topic_ES

        self.device = device
        # CLIENT_LOOP é colocado em uma thread para que o programa não entre em
        # loop e não bloqueia a adição de novos TOPICOS
        client_loop(self.client).start()

    def add_subscribe(self, topico):
        print(topico)
        self.client.subscribe(topico, 0)

    def on_connect(self, client, userdata, flags, rc):
        print(rc)

    def on_message(self, mosq, obj, msg):
        
        try:
            data = json.loads(msg.payload.decode("utf-8"))
        # print(msg.payload.decode("utf-8"))
            self.device.collect_data(data)
        # print(data)
        except Exception as e:
            print(str(e))
        # try:
        #     collect_data = self.collect_sensor(data["uuid"])
        #     # msg = '{"date": "2019-09-23 10:19:44", "uuid_gateway": "3aa027bd-4afc-461c-b353-c2535008f4ce", "uuid_edge": "b0013009-740b-4373-9aec-687c7818df06", "uuid_sensor": "a08042cf-8610-4bd4-8bea-6320ce7c613b", "data": 85.0, "type": "pub"}'
        #     self.on_publish(collect_data)
        # except Exception as e:
        #     print("Erro na mensagem recebida para coleta ou na coleta do dado")
        #     print(str(e))

    def on_publish(self, msg):
        self.client.publish(topic=self.topic_pub, payload=msg, qos=0, retain=False)

    # Simula um coleta do sensor, retornando um valor randomico
    def collect_sensor(self, uuid):
        valeu_sensor = random.uniform(20,25)

        # date_now = datetime.datetime.now()
        # date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
        
        msg = {"type": "collect", "uuid_sensor": uuid, "data": valeu_sensor}
        #msg = {"uuid": uuid, "data": valeu_sensor, "date": date_str}
        # convert into JSON:
        msg = json.dumps(msg) 

        return msg

class client_loop (Thread):
    def __init__(self,client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.loop_forever()