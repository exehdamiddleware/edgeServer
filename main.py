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
# from ipc import *

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


# Cria os objetos na seguinte ordem:
#	- Scheduler
#	- Event_treatment
#	- ipc   <----- Nesse componente é compartilhado os dois objetos criado acima

# event_treatment = Event_Treatment()
# scheduler = Scheduler(event_treatment)
scheduler = Scheduler()

# event_treatment.add_object_scheduler(scheduler)

# ipc = IPC(event_treatment, username_ES, password_ES, host_ES, port_ES)

# event_treatment.add_object_ipc(ipc)


# scheduler = Scheduler()
# event_treatment = Event_Treatment(scheduler)

# ipc = IPC(event_treatment, username_ES, password_ES, host_ES, port_ES)

# Utilizado para o compartilhamento dos metodos do Objeto IPC no event_treatment

# event_treatment.add_object(ipc)

# scheduler.add_object(event_treatment)

# Make a UUID using an MD5 hash of a namespace UUID and a name
# Realizando um IF para verificar a existencia do uuid_ES no DB
# uuid_ES = uuid.uuid3(uuid.NAMESPACE_DNS, 'middleware_EXEHDA')

# print("uuid_GW: ", uuid_ES)

