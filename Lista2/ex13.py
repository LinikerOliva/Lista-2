def ler_arquivo_texto(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

print(ler_arquivo_texto('arquivo.txt'))