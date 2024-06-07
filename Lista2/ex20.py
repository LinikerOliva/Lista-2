def vendedor_mais_e_menos_vendeu(nome_arquivo):
    with open(nome_arquivo, 'r', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        vendas_por_vendedor = {}
        for linha in leitor:
            vendedor, venda = linha
            if vendedor in vendas_por_vendedor:
                vendas_por_vendedor[vendedor] += float(venda)
            else:
                vendas_por_vendedor[vendedor] = float(venda)
        vendedor_mais_vendeu = max(vendas_por_vendedor, key=vendas_por_vendedor.get)
        vendedor_menos_vendeu = min(vendas_por_vendedor, key=vendas_por_vendedor.get)
        return vendedor_mais_vendeu, vendedor_menos_vendeu

print(vendedor_mais_e_menos_vendeu('vendas_por_vendedor.csv'))
