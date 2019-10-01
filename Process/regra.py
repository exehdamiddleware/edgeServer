
import psycopg2
import re

connection = psycopg2.connect(user = 'postgres', password = 'batata', host = "127.0.0.1", port = "5432", database = "teste")

cursor = connection.cursor()
postgreSQL_select_Query = "select * from rule where id = 1"

cursor.execute(postgreSQL_select_Query)
regra = cursor.fetchall() 
        
# print(regra[0][1]) 

temp = 20
# # regra = 'If temp > 30: print("entrou no if") else: print("nops")'
juca = 'if temp > 30: print("entrou no if")\nelse: print("nops")'

# print(str(juca) == str(regra[0][1]))
print(regra[0][1])
print(juca)


test = regra[0][1].replace("\\n", "\n")

print(test)
exec(juca)




# i=0
# teste = ''

# while i <= len(juca):
#  	if regra[0][1][i] == '\\':
#  		teste = teste + "\n"
#  		i = i+2
#  	else:
#  		teste = teste + regra[0][1][i] 
#  	i = i + 1

# print(teste)
# exec(teste)
# exec(regra[0][1])