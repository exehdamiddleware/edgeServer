# models.py

import peewee
# import threading

# Criamos o banco de dados
db = peewee.SqliteDatabase('edger_server.db')


class BaseModel(peewee.Model):
    """Classe model base"""

    class Meta:
        database = db


class Manufacturer(BaseModel):

    name = peewee.CharField(null=True)
    address = peewee.CharField(null=True)
    phone = peewee.CharField(null=True)
    url = peewee.CharField(null=True)
    city = peewee.CharField(null=True)
    state = peewee.CharField(null=True)
    country = peewee.CharField(null=True)

class Gateway(BaseModel):
    uuid = peewee.CharField(primary_key=True)
    name = peewee.CharField(null=True)
    status = peewee.BooleanField(null=True)

    manufacturer_id = peewee.ForeignKeyField(Manufacturer, null=True)

class Device(BaseModel):
    uuid = peewee.CharField(primary_key=True)
    name = peewee.CharField(null=True)
    description = peewee.CharField(null=True)
    model = peewee.CharField(null=True)
    precision = peewee.CharField(null=True)
    unit = peewee.CharField(null=True)
    pin = peewee.CharField(null=True)
    driver = peewee.CharField(null=True)
    manufacturer_id = peewee.ForeignKeyField(Manufacturer, null=True)
    gateway_id = peewee.ForeignKeyField(Gateway)

class Context_Server(BaseModel):
    uuid = peewee.CharField(primary_key=True)
    name = peewee.CharField(null=True)
    ip = peewee.CharField(null=True)
    port = peewee.CharField(null=True)
    user = peewee.CharField(null=True)
    password = peewee.CharField(null=True)

class Persistance(BaseModel):
    value = peewee.CharField(null=True)
    collect_date = peewee.CharField(null=True)
    publisher = peewee.BooleanField(null=True)
    device_uuid = peewee.ForeignKeyField(Device)

class Scheduler(BaseModel):
    event = peewee.CharField(null=True)
    second = peewee.CharField(null=True)
    minute = peewee.CharField(null=True)
    hour = peewee.CharField(null=True)
    day = peewee.CharField(null=True)
    month = peewee.CharField(null=True)
    year = peewee.CharField(null=True)
    device_uuid = peewee.ForeignKeyField(Device)

class Action_Rule(BaseModel):
    command = peewee.CharField(null=True)

class Rule(BaseModel):
    command = peewee.CharField(null=True)
    name = peewee.CharField(null=True)
    rule = peewee.CharField(null=True)
    action_rule_id = peewee.ForeignKeyField(Action_Rule)
    device_uuid = peewee.ForeignKeyField(Device)



# if __name__ == '__main__':
#     try:
#         Manufacturer.create_table()
#         print("Tabela 'Manufacturer' criada com sucesso!")
#     except peewee.OperationalError:
#         print("Tabela 'Manufacturer' ja existe!")

#     try:
#         Gateway.create_table()
#         print("Tabela 'Gateway' criada com sucesso!")
#     except peewee.OperationalError:
#         print("Tabela 'Gateway' ja existe!")

#     try:
#         Device.create_table()
#         print("Tabela 'Device' criada com sucesso!")
#     except peewee.OperationalError:
#         print("Tabela 'Device' ja existe!")

#     try:
#         Context_Server.create_table()
#         print("Tabela 'Context Server' criada com sucesso!")
#     except peewee.OperationalError:
#         print("Tabela 'Context Server' ja existe!")

#     try:
#         Persistance.create_table()
#         print("Tabela 'Persistance' criada com sucesso!")
#     except peewee.OperationalError:
#         print("Tabela 'Persistance' ja existe!")

#     try:
#         Scheduler.create_table()
#         print("Tabela 'Scheduler' criada com sucesso!")
#     except peewee.OperationalError:
#         print("Tabela 'Scheduler' ja existe!")

#     try:
#         Action_Rule.create_table()
#         print("Tabela 'Action_Rule' criada com sucesso!")
#     except peewee.OperationalError:
#         print("Tabela 'Action_Rule' ja existe!")

#     try:
#         Rule.create_table()
#         print("Tabela 'Rule' criada com sucesso!")
#     except peewee.OperationalError:
#         print("Tabela 'Rule' ja existe!")