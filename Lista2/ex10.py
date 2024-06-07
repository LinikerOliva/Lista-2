def frequencia_palavra(texto, palavra):
    palavras = texto.split()
    return palavras.count(palavra)

texto = 'Python é uma linguagem de programação. Python é poderoso.'
print(frequencia_palavra(texto, 'Python'))