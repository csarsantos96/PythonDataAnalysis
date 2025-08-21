import requests

def enviar_arquivo():
    caminho = "C:/Users/Cesar Santos/Downloads/jorgen-hendriksen-HsB4t2NvtLo-unsplash.jpg"

    with open(caminho, 'rb') as f:
        files = {'file': f}
        response = requests.post("https://file.io", files=files)

    try:
        response.raise_for_status()
        data = response.json()
        if data.get('success'):
            print(" Arquivo enviado com sucesso!")
            print("Link:", data['link'])
        else:
            print(" Algo deu errado:", data)
    except Exception as e:
        print(" Erro ao processar resposta:", e)
        print(" Resposta bruta:", response.text)

enviar_arquivo()
