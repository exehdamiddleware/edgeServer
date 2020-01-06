#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subscriber import *
from collect_device import *
import json
from read_json import *


# Para gerar uuid, entre no link: https://www.uuidgenerator.net

json_read = Read_JSON()
json = json_read.read("configuration")

# Informações dos sensores e gateway
sensors = json['sensors']
gateway = json['gateway']

# Informações de acesso ao Broker no Servidor de Borda
username_ES = json['broker_mqtt']['user']
password_ES = json['broker_mqtt']['password']
host_ES = json['broker_mqtt']['ip']
port_ES = json['broker_mqtt']['port']
topic_ES = json['broker_mqtt']['topic']

# Cria o objeto para a conexão com o Servidor de Borda
device = Collect_devide()
subscriber = Subscriber(device,username_ES,password_ES,host_ES,port_ES,topic_ES,sensors,gateway)

device.add_object_subscriber(subscriber)

# subscriber.on_publish()


# mosquitto_pub -t "GW_3aa027bd-4afc-461c-b353-c2535008f4ce" -u "middleware" -P "exehda" -h 127.0.0.1 -p 1883 -m '{"uuid": "a08042cf-8610-4bd4-8bea-6320ce7c613b"}'
# mosquitto_sub -t "contextserver" -u "middleware" -P "exehda" -h 127.0.0.1 -p 1883