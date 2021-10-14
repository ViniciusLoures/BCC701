while True:
    produto = str(input('Informe o nome do produto: ')).upper().strip()
    if produto == 'FIM':
        break
    valor = float(input('Valor do pedido: R$ '))
    if produto == 'PÃO DE QUEIJO':
        if valor <= 50:
            print('Percentual de desconto: 10.00%')
            print(f'Valor com desconto: R$ {(valor*0.9):.2f}')
        elif valor <= 100:
            print('Percentual de desconto: 12.00%')
            print(f'Valor com desconto: R$ {(valor * 0.88):.2f}')
        elif valor > 100:
            print('Percentual de desconto: 15.00%')
            print(f'Valor com desconto: R$ {(valor * 0.85):.2f}')
    elif produto == 'PASTEL DE ANGU':
        if valor <= 50:
            print('Percentual de desconto: 9.00%')
            print(f'Valor com desconto: R$ {(valor*0.91):.2f}')
        elif valor <= 100:
            print('Percentual de desconto: 10.00%')
            print(f'Valor com desconto: R$ {(valor * 0.9):.2f}')
        elif valor > 100:
            print('Percentual de desconto: 11.00%')
            print(f'Valor com desconto: R$ {(valor * 0.89):.2f}')