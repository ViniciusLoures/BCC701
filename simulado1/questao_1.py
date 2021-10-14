total = float(input('Defina o valor total da compra: R$ '))
if total <= 0:
    print('Erro: Valor total inválido.')
    quit()
elif total <= 250:
    total = total * 0.97
    print('Desconto de 3%.')
elif 250 < total <= 550:
    total = total * 0.94
    print('Desconto de 6%.')
elif 550 < total <= 750:
    total = total * 0.92
    print('Desconto de 8%.')
elif total > 750:
    total = total * 0.90
    print('Desconto de 10%.')
print(f'Valor com desconto: R$ {total:.2f}')
