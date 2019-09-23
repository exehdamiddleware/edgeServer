#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import _thread
from subscriber import *
from publisher import *
import time
import json


# Para gerar uuid, entre no link: https://www.uuidgenerator.net
# O tópico de publicação é o mesmo uuid, dessa forma garanto que dado sensor é publicado num único local 

# uuid = "3aa027bd-4afc-461c-b353-c2535008f4ce"

sub = Subscriber()
sub.add_subscribe("GW_3aa027bd-4afc-461c-b353-c2535008f4ce")
# sub.add_subscribe("GW")

config = '{"date": "2019-09-23 10:22:22", "gateway": [{"uuid": "3aa027bd-4afc-461c-b353-c2535008f4ce", "name": "GW1"}], "uuid_edge": "b0013009-740b-4373-9aec-687c7818df06", "type": "conf", "broker_mqtt": [{"port": 1883, "ip": "200.132.96.11", "user": "middleware", "password": "exehda"}], "network": [{"name": "computacao-LUPS", "password": "fuckyoutorrent"}], "sensors": [{"name": "sensor_1", "driver": "driver_temp", "status": true, "manufacturer": "", "pin": 19, "uuid": "a08042cf-8610-4bd4-8bea-6320ce7c613b", "type": ""}, {"name": "sensor_2", "driver": "driver", "status": true, "manufacturer": "", "pin": 19, "uuid": "b08042cf-8610-4bd4-8bea-6320ce7c613b", "type": ""}, {"name": "sensor_3", "driver": "driver_temp", "status": true, "manufacturer": "", "pin": 1, "uuid": "c08042cf-8610-4bd4-8bea-6320ce7c613b", "type": ""}]}'
# time.sleep(5) 


# #JSON
# msg = {"uuid": uuid}
# # convert into JSON:
# msg = json.dumps(msg)
# # Dados do gateway
pub = Publisher("127.0.0.1", 1883)
pub.on_publish(config, 'GW')