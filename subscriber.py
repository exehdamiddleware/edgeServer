#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A small example subscriber
"""
from threading import Thread
import paho.mqtt.client as paho
from publisher import *
import json
import datetime

class Subscriber(object):
    """docstring for subscriber."""
    def __init__(self):
        self.uuid = "a0013009-740b-4373-9aec-687c7818df06"
        self.port = 1883
        self.password = "exehda"
        self.username = "middleware"
        self.ip = "200.132.96.11"
        self.client = paho.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish

        self.client.username_pw_set(username=self.username, password= self.password)
        self.client.connect(host=self.ip, port=self.port)

        # CLIENT_LOOP é colocado em uma thread para que o programa não entre em
        # loop e não add novos TOPICOS
        client_loop(self.client).start()

    def add_subscribe(self, topico):
        self.client.subscribe(topico, 0)

    def on_connect(self, client, userdata, flags, rc):
        print(rc)

    def on_message(self, mosq, obj, msg):
        print("-------Enviando para SC-------")
        msg_json = msg.payload.decode("utf-8")
        msg_json = json.loads(msg_json)
        #print(msg_json)
        
        msg_json["edge"] = {}
        msg_json["edge"]["uuid"] = self.uuid
        msg_json["edge"]["username"] = self.username
        msg_json["edge"]["password"] = self.password
        msg_json["edge"]["ip"] = self.ip
        msg_json["edge"]["port"] = self.port
        msg_json["edge"]["name"] = "SB_1"

        print("---------Enviado--------")        
        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
        
        msg_json["date"] = date_str
       
        msg_json = json.dumps(msg_json)
     
        print(msg_json)
<<<<<<< HEAD
        #topic = "contextserver"
        topic = "ifarming"
        #topic = "exehda_ft"
        pub = Publisher("200.132.96.10", 1883)
=======
        topic = "edgeServer"

        # pub = Publisher("200.132.96.10", 1883)
        pub = Publisher("127.0.0.1", 1883)
>>>>>>> cbfacc3baa3ec52e5233125dfaa086c5d0a6d30e
        pub.on_publish(msg_json, topic)

        # print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def on_publish(self, mosq, obj, mid):
        #print("mid: "+str(mid))
        pass

class client_loop (Thread):
    def __init__(self,client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.loop_forever()
