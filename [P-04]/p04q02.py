# Vinicius Alves Loures França 20.1.1039
strawberry = float(input('Quantidade de Morangos (em kg): '))
apple = float(input('Quantidade de Maçãs (em kg): '))
total = 0
if 0 <= strawberry <= 5:
    total = total + (strawberry * 2.5)
elif strawberry > 5:
    total = total + (strawberry * 2.2)
else:
    print('Entrada inválida')
    quit()
if 0 <= apple <= 5:
    total = total + (apple * 1.8)
elif apple > 5:
    total = total + (apple * 1.5)
else:
    print('Entrada inválida')
    quit()
print(f'O valor total da sua compra é R$ {total:.2f}')
