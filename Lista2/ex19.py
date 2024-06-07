def soma_vendas_por_vendedor(nome_arquivo):
    with open(nome_arquivo, 'r', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        vendas_por_vendedor = {}
        for linha in leitor:
            vendedor, venda = linha
            if vendedor in vendas_por_vendedor:
                vendas_por_vendedor[vendedor] += float(venda)
            else:
                vendas_por_vendedor[vendedor] = float(venda)
        return vendas_por_vendedor

print(soma_vendas_por_vendedor('vendas_por_vendedor.csv'))
