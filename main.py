#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scheduler import *
from event_treatment import *
from ipc import *

from read_json import *

json_read = Read_JSON()
jsonR = json_read.read("configuration")

name_ES = jsonR['edge_server']['name']
uuid_ES = jsonR['edge_server']['uuid']

# Informações de acesso ao Broker no Servidor de Contexto
username_CS = jsonR['broker_mqtt_CS']['user']
password_CS = jsonR['broker_mqtt_CS']['password']
host_CS = jsonR['broker_mqtt_CS']['ip']
port_CS = jsonR['broker_mqtt_CS']['port']

# Informações de acesso ao Broker no Servidor de Borda
username_ES = jsonR['broker_mqtt_ES']['user']
password_ES = jsonR['broker_mqtt_ES']['password']
host_ES = jsonR['broker_mqtt_ES']['ip']
port_ES = jsonR['broker_mqtt_ES']['port']

# Lista de tópicos
topics = jsonR['topics']
topics.append("ES_"+uuid_ES)

# mosquitto_sub -t "GW_3aa027bd-4afc-461c-b353-c2535008f4ce" -u "middleware" -P "exehda" -h 127.0.0.1 -p 1883


# Cria os objetos na seguinte ordem:
#	- Event Treatment
#	- Scheduler
#	- IPC

event_treatment = Event_Treatment(jsonR)
scheduler = Scheduler_Edge_Server(event_treatment)
event_treatment.add_object_scheduler(scheduler)

ipc = IPC(event_treatment, username_CS, password_CS, host_CS, port_CS, username_ES, password_ES, host_ES, port_ES, topics)

event_treatment.add_object_ipc(ipc)



msg = {'edge_server': {'uuid':jsonR['edge_server']['uuid'], 'name':jsonR['edge_server']['name'], 'user':jsonR['broker_mqtt_ES']['user'], 'password':jsonR['broker_mqtt_ES']['password'], 'ip':jsonR['broker_mqtt_ES']['ip'], 'port':jsonR['broker_mqtt_ES']['port']}}

ipc.on_publish_CS("ES", json.dumps(msg))



# Make a UUID using an MD5 hash of a namespace UUID and a name
# Realizando um IF para verificar a existencia do uuid_ES no DB
# uuid_ES = uuid.uuid3(uuid.NAMESPACE_DNS, 'middleware_EXEHDA')

# print("uuid_GW: ", uuid_ES)