
import json
import datetime

class Device_Process(object):
    ipc = None

    def __init__(self, ipc):
        self.ipc = ipc

    # Realiza uma busca no DB realacionando o sensor com o GW em busca do uuid
    # Topico de publisher GW_ + (uuid do GW)
    def process(self, data, topic=None):
        
        # Dado é enviado para o CS com o topico recebido 
        if topic:
            
            date_now = datetime.datetime.now()
            date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
  
            data["date"] = date_str

            data = json.dumps(data)

            self.ipc.on_publish_CS(topic, data)

        # É feita uma "requisição" para um determinado device
        else:
            #Acesso ao DB em busca do uuid do GW
            uuid_GW = "3aa027bd-4afc-461c-b353-c2535008f4ce"

            # Topic de publicação do gateway e mensagem a ser enviada
            topic = "GW_" + uuid_GW
            msg = {'uuid': data}
            msg = json.dumps(msg)

            # Envia mensagem para o topico especifico, enviando para GW em questão
            self.ipc.on_publish_ES(topic, msg)

    def process_configuration(self, data, topic, configuration):

        # print("DEVICE")

        data["edge"] = {}
        data["edge"]["uuid"] = configuration['edge_server']['uuid']
        data["edge"]["username"] = configuration['broker_mqtt_ES']['user']
        data["edge"]["password"] = configuration['broker_mqtt_CS']['password']
        data["edge"]["ip"] = configuration['broker_mqtt_CS']['ip']
        data["edge"]["port"] = configuration['broker_mqtt_CS']['port']
        data["edge"]["name"] = configuration['edge_server']['name']

        msg = json.dumps(data)

        self.ipc.on_publish_CS(topic, msg)