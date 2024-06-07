import random

def embaralhar(lista):
    copia_lista = lista.copy()
    random.shuffle(copia_lista)
    return copia_lista

print(embaralhar([1, 2, 3, 4, 5]))