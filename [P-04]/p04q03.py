# Vinicius Alves Loures França 20.1.1039
from math import sqrt
q = int(input('Digite a quantidade de lados: '))
if q in (3, 4, 5):
    side = float(input('Digite a medida do lado: '))
    if q == 3:
        a = (side ** 2 * sqrt(3)) / 4
        print(f'O polígono é um triângulo com área: {a:.2f}')
    elif q == 4:
        a = side ** 2
        print(f'O polígono é um quadrado com área: {a:.2f}')
    elif q == 5:
        a = (3 * side ** 2 * sqrt(3)) / 2
        print(f'O polígono é um pentágono com área: {a:.2f}')
elif q < 3:
    print('Não é um polígono')
elif q > 5:
    print('Polígono não identificado')
