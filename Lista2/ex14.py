import csv

def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, 'r', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        return [linha for linha in leitor]

print(ler_arquivo_csv('arquivo.csv'))