def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos(lista):
    return [numero for numero in lista if eh_primo(numero)]

print(numeros_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))