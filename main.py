#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
# import _thread
#from subscriber_2 import *
#from publisher import *
# import time
# import json
from ipc import *
import uuid

# https://www.w3schools.com/python/python_json.asp

# Para gerar uuid, entre no link: https://www.uuidgenerator.net
# O tópico de publicação é o mesmo uuid, dessa forma garanto que dado sensor é publicado num único local 
# sensor_uuid = "3aa027bd-4afc-461c-b353-c2535008f4ce"
# gw_uuid = "3aa027bd-4afc-461c-b353-c2535008f4ce"


# Informações de acesso ao Broker no Servidor de Contexto
username_CS = "middleware"
password_CS = "exehda"
host_CS = "127.0.0.1"
port_CS = 1883

# Informações de acesso ao Broker no Servidor de Borda
username_ES = "middleware"
password_ES = "exehda"
host_ES = "127.0.0.1"
port_ES = 1883

#
ipc = IPC(username_ES, password_ES, host_ES, port_ES)

# Make a UUID using an MD5 hash of a namespace UUID and a name
# Realizando um IF para verificar a existencia do uuid_ES no DB
uuid_ES = uuid.uuid3(uuid.NAMESPACE_DNS, 'middleware_EXEHDA')

print(uuid_ES)

