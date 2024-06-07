def menor_string(lista):
    return min(lista, key=len)

print(menor_string(['Python', 'Java', 'C', 'JavaScript', 'Ruby']))