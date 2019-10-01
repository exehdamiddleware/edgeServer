import psycopg2
import re


# Conecta no DB e pega a regra do DB
# connection = psycopg2.connect(user = 'postgres', password = 'batata', host = "127.0.0.1", port = "5432", database = "contexserver2")
connection = psycopg2.connect(user = 'postgres', password = 'batata', host = "127.0.0.1", port = "5432", database = "contextserver2")

cursor = connection.cursor()
postgreSQL_select_Query = "select * from rule where id = 1"

cursor.execute(postgreSQL_select_Query)
regra = cursor.fetchall() 
# print(regra[0][1])

# Verifica os as palavras chave em busca dos sensores
words = regra[0][1].split(' ')


for x in range(len(words)):
	if words[x].find("#") != -1:
		postgreSQL_select_Query = "select row_to_json(publicacoes) from publicacoes where sensor_uuid = '"+words[x].replace('#', '')+"'"
		print(postgreSQL_select_Query)

		cursor.execute(postgreSQL_select_Query)
		data_sensor = cursor.fetchall()
		# print(data_sensor[0][0]['publicacao_id'])
		words[x] = str(data_sensor[0][0]['valorcoletado'])
# 		sensors.append(words[x].replace('#', ''))






# 


# sensors = []

# for x in range(len(words)):
# 	if words[x].find("#") != -1:
# 		# words[x] = "sensor_1"
# 		sensors.append(words[x].replace('#', ''))

words = ' '.join(words)

# print(words)

# words.replace("\n", "/\n")

print(words)


test = words.replace(" \\n ", "\n")

print(test)

exec(test)



# i=0
# teste = ''

# while i <= len(words):
#  	if words[i] == '\\':
#  		teste = teste + "/\n"
#  		i = i+2
#  	else:
#  		teste = teste + words[i] 
#  	i = i + 1

# print(teste)



# exec(words)

# for idx, val in enumerate(words):
#     print(idx, val)

# Após a busca do sensores, pega os dados no DB
# for sensor in sensors:
# 	postgreSQL_select_Query = "select * from publicacoes where uuid = "+sensor
# 	print(postgreSQL_select_Query)

# print(sensors)
# print(words)

# for sensor in sensors:
# 	postgreSQL_select_Query = "select row_to_json(publicacoes) from publicacoes where sensor_uuid = '"+sensor+"'"
# 	# print(postgreSQL_select_Query)

# 	cursor.execute(postgreSQL_select_Query)
# 	data_sensor = cursor.fetchall()

# 	print(data_sensor[0][0]['publicacao_id'])


# Substitui os dados na regra


# Executa a regra