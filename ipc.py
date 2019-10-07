

import paho.mqtt.client as paho
from threading import Thread


class IPC(object):
    """docstring for IPC"""
    def __init__(self, username, password, host, port):
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

    def on_message(self, mosq, obj, msg):
        print(msg.payload.decode("utf-8"))
        print("=========================")

    def on_publish(self, mosq, obj, mid):
        pass

class client_loop (Thread):
    def __init__(self,client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.loop_forever()
            