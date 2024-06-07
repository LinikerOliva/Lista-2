import json

def ler_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return json.load(arquivo)

print(ler_arquivo_json('arquivo.json'))
