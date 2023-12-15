def calcular_valor_pedido(itens_pedido):
    valor_itens = sum(item['quantidade'] * item['valor_unitario'] for item in itens_pedido)
    valor_frete = valor_itens * 0.1 if valor_itens < 500 else 0
    valor_total = valor_itens + valor_frete
    return valor_itens, valor_frete, valor_total

def processar_pedido(pedido):
    nome_cliente = pedido['cliente']
    itens_pedido = pedido['itens']

    valor_itens, valor_frete, valor_total = calcular_valor_pedido(itens_pedido)

    print(f"Cliente: {nome_cliente}")
    print(f"Valor dos itens: R${valor_itens:.2f}")
    print(f"Valor do frete: R${valor_frete:.2f}")
    print(f"Valor total do pedido: R${valor_total:.2f}")
    print()

# Exemplo de uso:

# Dados dos pedidos
pedidos = [
    {
        'cliente': 'Cliente1',
        'data': '2023-01-01',
        'fidelidade': True,
        'itens': [
            {'produto': 'Produto1', 'quantidade': 2, 'valor_unitario': 50.00},
            {'produto': 'Produto2', 'quantidade': 1, 'valor_unitario': 30.00}
        ]
    },
    {
        'cliente': 'Cliente2',
        'data': '2023-02-15',
        'fidelidade': False,
        'itens': [
            {'produto': 'Produto3', 'quantidade': 3, 'valor_unitario': 20.00},
            {'produto': 'Produto4', 'quantidade': 1, 'valor_unitario': 40.00}
        ]
    },
]

# Processar e exibir informações de cada pedido
for pedido in pedidos:
    processar_pedido(pedido)
