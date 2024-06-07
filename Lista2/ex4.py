def contar_ocorrencias(frase, palavra):
    return frase.split().count(palavra)


print(contar_ocorrencias('Python é uma linguagem de programação poderosa', 'linguagem'))