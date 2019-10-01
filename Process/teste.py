from bs4 import BeautifulSoup 
import requests 
import sys 
import re

url = "https://cnpj.biz/procura/vantum"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

# print(soup)

# for a in soup.findAll('a',{'class':'link url'}):#href=True):    # Procura dentro o códido HTML essa conf, para depois encontrar o link
#         print(a)

# for a in soup.findAll('CNPJ'):#href=True):    # Procura dentro o códido HTML essa conf, para depois encontrar o link
    # print(a)

# r1 = re.findall(r"^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$",r.text)
# print(r1)

m = re.search(r'CNPJ', r.text)
if m:
	print(m.span())
	print('foi')


CNPJ = 18

# def parse_input(i):
#     'Retira caracteres de separação do CNPJ'

#     i = str(i)
#     i = i.replace('.', '')
#     i = i.replace(',', '')
#     i = i.replace('/', '')
#     i = i.replace('-', '')
#     i = i.replace('\\', '')
#     return i


# Para CNPJ
# /^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$/