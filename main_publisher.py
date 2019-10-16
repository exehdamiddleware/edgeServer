#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import _thread
# from subscriber import *
from publisher import *
import time
import json

# https://www.w3schools.com/python/python_json.asp

# Para gerar uuid, entre no link: https://www.uuidgenerator.net
# O tópico de publicação é o mesmo uuid, dessa forma garanto que dado sensor é publicado num único local 
sensor_uuid = "a08042cf-8610-4bd4-8bea-6320ce7c613b"
gw_uuid = "3aa027bd-4afc-461c-b353-c2535008f4ce"

# JSON é composto pelos dados da borda, ip e port, e uuid do sensor
# msg = {'uuid': sensor_uuid}
msg = '{"type": "scheduler","modo": "cron","task": {"type": "device", "uuid":"a08042cf-8610-4bd4-8bea-6320ce7c613b"},"second":"*/5", "minute":"*", "hour":"*", "day":"*", "month":"*", "year":"*" }'

# msg = '{"type": "configuration","version": 1,"network":{"name": "LUPS-2","password": "Lups@2019"},"gateway":{"name": "GW1","uuid": "3aa027bd-4afc-461c-b353-c2535008f4ce"},"broker_mqtt":{"ip":"200.132.96.11","port":1883,"user":"middleware","password":"exehda"},"sensors":[{"name":"sensor_1","uuid":"a08042cf-8610-4bd4-8bea-6320ce7c613b","driver":"driver_temp","pin":19,"manufacturer":"","type":"","status":true},{"name":"sensor_2","uuid":"b08042cf-8610-4bd4-8bea-6320ce7c613b","driver":"driver_temp","pin":21,"manufacturer":"","type":"","status":true},{"name":"sensor_3","uuid":"c08042cf-8610-4bd4-8bea-6320ce7c613b","driver":"driver_ldr","pin":32,"manufacturer":"","type":"","status":true},{"name":"reset","uuid":"d08042cf-8610-4bd4-8bea-6320ce7c613b","driver":"reset","pin":32,"manufacturer":"","type":"","status":true}]}'


# convert into JSON:
# msg = json.dumps(msg)

# Dados do gateway
# topic = "GW_"+gw_uuid
topic = "ES_76a69636-6495-4eec-be4f-b40fb2fb3b22"


pub = Publisher("127.0.0.1", 1883)

pub.on_publish(msg, topic)
# conta =0
# while(conta < 10):

# i=0
# while(i < 10):
# 	pub.on_publish(msg, topic)
# 	time.sleep(30)
# 	i = i+1
# conta = conta +1
