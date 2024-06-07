def maiores_elementos(lista, k):
    return sorted(lista, reverse=True)[:k]


print(maiores_elementos([1, 5, 3, 9, 7, 2], 3))