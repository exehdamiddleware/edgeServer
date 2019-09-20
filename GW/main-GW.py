#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import _thread
from subscriber import *
# from publisher import *
import time
import json


# Para gerar uuid, entre no link: https://www.uuidgenerator.net
# O tópico de publicação é o mesmo uuid, dessa forma garanto que dado sensor é publicado num único local 

# uuid = "3aa027bd-4afc-461c-b353-c2535008f4ce"

sub = Subscriber()
sub.add_subscribe("GW_3aa027bd-4afc-461c-b353-c2535008f4ce")

# time.sleep(5) 


# #JSON
# msg = {"uuid": uuid}
# # convert into JSON:
# msg = json.dumps(msg)

# # Dados do gateway
# pub = Publisher("127.0.0.1", 1883)
# pub.on_publish(msg, uuid)