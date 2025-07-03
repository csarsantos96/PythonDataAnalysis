import requests

def enviar_arquivo():

    #Caminho do arquivo para upload
    caminho = 'C:/Users/Cesar Santos/Downloads/jorgen-hendriksen-HsB4t2NvtLo-unsplash.jpg'

    #Enviar arquivo

    requisicao = requests.post('https://file.io', files={'image': open(caminho, 'rb')}) # rb = read binary
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print("Arquivo enviado, link para acesso:", url)

    enviar_arquivo()