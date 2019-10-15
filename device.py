
import json

class Device(object):

    ipc = None

    def __init__(self, ipc, uuid):
        self.ipc = ipc
        self.uuid_device = uuid

        self.collect()

    # Realiza uma busca no DB realacionando o sensor com o GW em busca do uuid
    # Topico de publisher GW_ + (uuid do GW)
    def collect(self):
        # Acesso ao DB em busca do uuid do GW
        uuid_GW = "3aa027bd-4afc-461c-b353-c2535008f4ce"

        # Topic de publicação do gateway e mensagem a ser enviada
        topic = "GW_"+uuid_GW
        msg = {'uuid': self.uuid_device}
        msg = json.dumps(msg)

        # Envia mensagem para o topico especifico, enviando para GW em questão
        self.ipc.on_publish(topic, msg)