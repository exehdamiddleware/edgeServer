
import json

class Device(object):

    ipc = None

    def __init__(self, ipc, uuid):
        self.ipc = ipc
        self.uuid_device = uuid
        # print(uuid)

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


        # print(self.uuid_device)





    # def regra(self,json_result_gathering):   # Verifica argumentos e criar objeto p chamar regras
    #     engine = EngineRule(self.core)

    #     string_rule = '{{ "evento": "e", "id": "{0}","valor": {1}, "id_gateway": {2} }}'.format(json_result_gathering['id_sensor'],json_result_gathering['value'],json_result_gathering['id_gateway'],json_result_gathering['collectDate'])
    #     #print(string_rule)
    #     #print("chegou no gathering, vai chamar regra")
    #     engine.run_rules(string_rule)

    # def processamento(self, jsonObject): # 0 = OBJECT or 1 = FUNCTION
    #                             # Cria um objeto COMMUNICATION, que retorna um valor do sensor
    #                             # Realiza um if, verificando se precisa criar um  REGRA ou apenas
    #                             # retorna um dado
    #     colecter_sensor = Communication(self.core)
    #     formation = colecter_sensor.get_values_on_gatway(jsonObject)            #
    #     #print("======================Gathering======================")
    #     #print(jsonObject)
    #     #print("=====================================================")

    #     if jsonObject['collect_to_rule']:
    #         return formation
    #     else:
    #         try:
    #             self.regra(formation)
    #             return None
    #         except TypeError:
    #             print("ARGUMENTO REGRA NULL - VERIFICAR ACESSO AO GETWAY")
    #             return None
    #         except:
    #             print("ERRO NO GATHERING - VERIFICAR TIPO DE ERRO")
    #             return None