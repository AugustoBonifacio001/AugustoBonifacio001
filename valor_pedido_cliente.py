def calcular_valor(itens_pedido):
     valor_itens = sum(item['quantidade'] * item['valor_unitario'] for item in itens_pedido)
     valor_frete = valor_itens * 0.1 if valor_itens < 500 and not cliente_fidelidade else 0
     valor_total = valor_itens + valor_frete
     return valor_itens, valor_frete, valor_total

pedidos = []

while True:
    # Ler os dados dos pedido
    nome_cliente = input("Nome do cliente ( ou ' sair' para encerrar):").lower()
    if nome_cliente == 'sair':
        break

    data_pedido = input("Data do pedido :")
    cliente_fidelidade = input("É cliente fidelidade ? (S/N):").upper() == 'S'

    # Ler os items do pedido 
    # Será usado o método append para adicionar os pares chave-valor do dicionário à lista items_pedido
    itens_pedido = []

    while True:
        nome_do_produto = input("Qual o nome do produto (ou ' sair' para encerrar):")
        if nome_do_produto.lower() == 'sair':
            break
        quantidade = int(input("Quantidade:"))
        valor_unitario = float(input("Valor unitário:"))

        item= {'nome do produto': nome_do_produto, 'quantidade': quantidade, 'valor_unitario': valor_unitario }
        itens_pedido.append(item)

    # Calcular os dados do pedido
    # Serão utilizados métodos de desempacotamento de tuplas
    valor_itens, valor_frete, valor_total = calcular_valor(itens_pedido)

    # Os dados serão armazenados utilizando dicionários, tais dados serão acrescentados à lista pedidos.


    pedido = {
       
        'nome_cliente': nome_cliente,
        'data_pedido': data_pedido,
        'cliente_fidelidade': cliente_fidelidade,
        'itens_pedido': itens_pedido,
        'valor_itens': valor_itens,
        'valor_frete': valor_frete,
        'valor_total': valor_total
    }

    pedidos.append(pedido)
    
    # Utilizando o for irá haver uma iteração em cada índice correspondente.
for pedido in pedidos:
    print("\nNome do Cliente:", pedido['nome_cliente'])
    print("Valor dos Itens:", pedido['valor_itens'])
    print("Valor do Frete:", pedido['valor_frete'])
    print("Valor Total do Pedido:", pedido['valor_total'])