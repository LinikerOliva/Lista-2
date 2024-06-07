import os

def consolidar_arquivos_texto(diretorio):
    conteudo = ''
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.txt'):
            with open(os.path.join(diretorio, arquivo), 'r') as f:
                conteudo += f.read() + '\n'
    return conteudo

print(consolidar_arquivos_texto('diretorio'))
