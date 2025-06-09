import requests
from bs4 import BeautifulSoup

url = 'https://python.org.br/cientifico/'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

#Exibir texto
#print(extracao.text.strip())

#Filtrar a exibição pela tag
# for linha_texto in extracao.find_all(['a','p']):
#     links = linha_texto.text.strip()
#     print('links: ', links)
#
# #contar quantidade de links  e parágrafos
# contar_links = 0
# contar_paragrafos = 0
#
# for linja_texto in extracao.find_all(['p', 'a']):
#     if linha_texto.name == 'a':
#         contar_links += 1
#     elif linha_texto.name == 'p':
#         contar_paragrafos += 1
# print('Total de links: ', contar_links)
# print('Total de paragrafos: ', contar_paragrafos)

# # Exibir somente o texto das tags h2 e p
# for linja_texto in extracao.find_all(['p', 'a']):
#     if linha_texto.name == 'a':
#         links = linha_texto.text.strip()
#         print('Links: \n', links)
#     elif linha_texto.name == 'p':
#         paragrafo = linha_texto.text.strip()
#         print('Paragrafo: \n', paragrafo)

# Exibir tags Aninhada
for titulo in extracao.find_all('h3'):
    print('\nTitulo:', titulo.text.strip())


    paragrafo = titulo.find_next_sibling('p')
    if paragrafo:
        for a in paragrafo.find_all('a', href=True):
            print('Texto Link:', a.text.strip(), '| URL:', a['href'])