#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scheduler import *
# import threading
# import _thread
# from subscriber_2 import *
# from publisher import *
# import time
# import json
# import uuid
# from scheduler import *
from event_treatment import *
from ipc import *

from read_json import *

json_read = Read_JSON()
json = json_read.read("string")

name_ES = json['edge_server']['name']
uuid_ES = json['edge_server']['uuid']

# Informações de acesso ao Broker no Servidor de Contexto
username_CS = json['broker_mqtt_CS']['user']
password_CS = json['broker_mqtt_CS']['password']
host_CS = json['broker_mqtt_CS']['ip']
port_CS = json['broker_mqtt_CS']['port']

# Informações de acesso ao Broker no Servidor de Borda
username_ES = json['broker_mqtt_ES']['user']
password_ES = json['broker_mqtt_ES']['password']
host_ES = json['broker_mqtt_ES']['ip']
port_ES = json['broker_mqtt_ES']['port']

# Lista de tópicos
topics = json['topics']
topics.append("ES_"+uuid_ES)

# mosquitto_sub -t "GW_3aa027bd-4afc-461c-b353-c2535008f4ce" -u "middleware" -P "exehda" -h 127.0.0.1 -p 1883


# Cria os objetos na seguinte ordem:
#	- Scheduler
#	- Event_treatment
#	- ipc   <----- Nesse componente é compartilhado os dois objetos criado acima

event_treatment = Event_Treatment(json)
scheduler = Scheduler_Edge_Server(event_treatment)
event_treatment.add_object_scheduler(scheduler)

ipc = IPC(event_treatment, username_CS, password_CS, host_CS, port_CS, username_ES, password_ES, host_ES, port_ES, topics)

event_treatment.add_object_ipc(ipc)



# Make a UUID using an MD5 hash of a namespace UUID and a name
# Realizando um IF para verificar a existencia do uuid_ES no DB
# uuid_ES = uuid.uuid3(uuid.NAMESPACE_DNS, 'middleware_EXEHDA')

# print("uuid_GW: ", uuid_ES)

