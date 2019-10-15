# import json
import threading
# import time
# from core.event_treatment import *
# import random
from apscheduler.schedulers.background import BackgroundScheduler


class Scheduler(object):

    # event_treatment = None

    # def __init__(self, object_event_treatment):
    #     print("SCHEDULER")
    #     self.event_treatment = object_event_treatment
    #     # Instância um agendador no background
    #     self.scheduler = BackgroundScheduler()
    #     self.scheduler.start()

    def __init__(self):
        print("Scheduler")
        # Instância um agendador no background
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def add_object(self, object_event_treatment=None):
        print("ADD Event")
        # self.event_treatment = object_event_treatment

    def add_job(self, jsonObject):   
        print("jsonObject")

        if jsonObject['modo'] == 'cron':
            jsonObject['type'] = jsonObject['task']['type']

            try:
                self.scheduler.add_job(self.function, jsonObject['modo'], second = jsonObject['second'], minute = jsonObject['minute'], 
                    hour = jsonObject['hour'], day = jsonObject['day'], month = jsonObject['month'], year = jsonObject['year'], 
                    id = str(jsonObject['task']['uuid']), args = [jsonObject],max_instances=50,misfire_grace_time=120)
            except:
                print("Não foi possível cadastrar o agendamento")
        else:
            print("Tarefa diferente do cron")

    def function(self, jsonObject):
        print("Dispertando evento")
        pass
        # self.event_treatment.process_event(jsonObject)
        
    

    #'{"modo": "cron","task": {"type": "sensor", "id":"51651565641651"},"second":"*/5", "minute":"*", "hour":"*", "day":"*", "month":"*", "year":"*" }'

        #self.create_job_check_persistence()

        #self.check_scheduler_reactivave()

    # def add_job(self, jsonObject): # cria uma nova tarefa no escalonador
    #     #print(type(jsonObject['status']))
    #     # jsonObject['collect_to_rule'] = False
    #     # if (jsonObject['status'] == 'True'or jsonObject['status'] == True):
    #     #     if jsonObject['id'] != '0':
    #     #         #print("ADICIONOU SENSOR")
    #     #         try:
    #     #             #print('klhashjkah')
    #     #             self.scheduler.add_job(self.function, jsonObject['modo'], second = jsonObject['second'], minute = jsonObject['minute'],
    #     #             hour = jsonObject['hour'], day = jsonObject['day'], month = jsonObject['month'], year = jsonObject['year'], id = str(jsonObject['id']), args = [jsonObject],max_instances=50,misfire_grace_time=120)
    #     #         except:     # Utilizado quando tem uma tarefa com ID para reescalonar
    #     #             self.scheduler.reschedule_job(jsonObject['id'], trigger='cron', second = jsonObject['second'],  minute = jsonObject['minute'],hour = jsonObject['hour'], day = jsonObject['day'], month = jsonObject['month'], year = jsonObject['year'])

    #     #     else:
    #     #         self.scheduler.add_job(self.check_persistence, jsonObject['modo'], second = jsonObject['second'], minute = jsonObject['minute'],
    #     #         hour = jsonObject['hour'], day = jsonObject['day'], month = jsonObject['month'], year = jsonObject['year'], id = jsonObject['id'], max_instances=1,misfire_grace_time=120)

    # def remove_job(self, jsonObject):    # id_tarefa - É ID do sensor/atuador a ser removido do CRON
    #     self.scheduler.remove_job(jsonObject['id'])

    # def function(self, jsonObject):        # response - É JSON passado como argumento

    #     #print(jsonObject['id'])
    #     #print("SENSOR ADD"+jsonObject['id_sensor'])
    #     object_events = Event_Treatment(self.core)
    #     object_events.event(jsonObject)

    # def check_persistence(self):# Modificar
    #     print("Tentou publicar a persistencia")
    #     persistence_publisher = Publisher(self.core)
    #     persistence_publisher.start()

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# Adiciona uma TAREFA no CRON, tornando resposavél pela publicação no contexto
# quando não ocorreu com sucesso este ato no módulo de gathering.

    # def create_job_check_persistence(self):  # Cria um JSON no formato exato que SCHEDULER
    #                                 # irá utilizar. QQ tratamento deve ocorrer aqui.
    #     job = {}

    #     job['modo'] = "cron"
    #     job['id'] = "0"
    #     job['status'] = "True"

    #     job['second'] = "*/30"
    #     #job['second'] = "0"
    #     #job['minute']  = "*/10"
    #     job['minute']  = "*"
    #     job['hour'] = "*"
    #     job['day'] = "*"
    #     job['week'] = "*"
    #     job['month'] = "*"
    #     job['year'] = "*"

    #     self.add_job(job)

    # def check_scheduler_reactivave(self):
    #     # print("check_scheduler_reactivave")

    #     try:
    #         #print("check_scheduler_reactivave   TRY")
    #         jsonSchedules = self.core.API_access("get", "schedules").json()
    #         print(jsonSchedules)

    #         for schedule in jsonSchedules:
    #             schedule['modo'] = 'cron'
    #             print(schedule)
    #             self.add_job(schedule)

    #     except Exception as inst:
    #         #print("check_scheduler_reactivave   EXCEPTION")
    #         #print(type(inst))
    #         time.sleep(10)
    #         self.check_scheduler_reactivave()

    #     except:
    #         print("PODE SER ERRO DE ACESSO POR CAUSA DE TOKEN INVALIDO")

    #     #print("check_scheduler_reactivave2")