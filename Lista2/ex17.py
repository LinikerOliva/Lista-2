def mes_com_mais_vendas(nome_arquivo):
    with open(nome_arquivo, 'r', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        vendas_por_mes = {linha[0]: int(linha[1]) for linha in leitor}
        return max(vendas_por_mes, key=vendas_por_mes.get)

print(mes_com_mais_vendas('vendas.csv'))
