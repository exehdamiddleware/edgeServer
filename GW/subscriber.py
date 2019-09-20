#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A small example subscriber
"""
from threading import Thread
import paho.mqtt.client as paho
import random
import json
import datetime

class Subscriber(object):
    """docstring for subscriber."""
    def __init__(self):

        self.client = paho.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.username_pw_set(username="middleware", password="exehda")

        self.client.connect("127.0.0.1", 1883)

        # CLIENT_LOOP é colocado em uma thread para que o programa não entre em
        # loop e não add novos TOPICOS
        client_loop(self.client).start()

    def add_subscribe(self, topico):
        self.client.subscribe(topico, 0)

    def on_connect(self, client, userdata, flags, rc):
        print(rc)

    def on_message(self, mosq, obj, msg):
        data = msg.payload.decode("utf-8")
        print(data)

        # data = json.loads(data)
        # collect_data = self.collect_sensor(data["uuid"])
        msg = '{"uuid_edge": "20", "data": 85.0, "type": "pub", "uuid_gw": "a08042cf-8610-4bd4-8bea-6320ce7c613b"}'

        self.on_publish("127.0.0.1", 1883, "GW", msg)

    def on_publish(self, ip, port, topic, msg):
        # self.client.connect(ip, port)
        print("INDO")
        self.client.publish(topic=topic, payload=msg, qos=0, retain=False)

    # Simula um coleta do sensor, retornando um valor randomico
    def collect_sensor(self, uuid):
        valeu_sensor = random.uniform(10,20)

        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
        # information_of_sensor['collectDate']  = date_str
       
        msg = {"uuid": uuid, "data": valeu_sensor, "date": date_str}
        # convert into JSON:
        msg = json.dumps(msg) 

        return msg

class client_loop (Thread):
    def __init__(self,client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.loop_forever()