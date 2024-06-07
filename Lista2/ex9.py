def encontrar_par_soma(lista, valor):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == valor:
                return lista[i], lista[j]
    return None

print(encontrar_par_soma([1, 2, 3, 4, 5], 7))