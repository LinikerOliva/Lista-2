def mes_com_menos_vendas(nome_arquivo):
    with open(nome_arquivo, 'r', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        vendas_por_mes = {linha[0]: int(linha[1]) for linha in leitor}
        return min(vendas_por_mes, key=vendas_por_mes.get)

print(mes_com_menos_vendas('vendas.csv'))
