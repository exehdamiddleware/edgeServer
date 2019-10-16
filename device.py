
import json

class Device_Process(object):
    ipc = None

    def __init__(self, ipc):
        self.ipc = ipc

    # Realiza uma busca no DB realacionando o sensor com o GW em busca do uuid
    # Topico de publisher GW_ + (uuid do GW)
    def process(self, data, topic=None):
        # print(topic)
        if topic:
            self.ipc.on_publish_CS(topic, data)

        else:
            #Acesso ao DB em busca do uuid do GW
            uuid_GW = "3aa027bd-4afc-461c-b353-c2535008f4ce"

            # Topic de publicação do gateway e mensagem a ser enviada
            topic = "GW_" + uuid_GW
            msg = {'uuid': data}
            msg = json.dumps(msg)

            # Envia mensagem para o topico especifico, enviando para GW em questão
            self.ipc.on_publish_CS(topic, msg)