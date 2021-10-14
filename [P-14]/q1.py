# Vinicius Alves Loures França 20.1.1039
from math import sqrt


def comprimento(reta):
    c = (reta['pontoB']['x'] - reta['pontoA']['x'])**2 + (reta['pontoB']['y'] - reta['pontoA']['y'])**2
    return sqrt(c)


quant = int(input('Informe a quantidade de retas: '))
retas = []
for i in range(quant):
    a = {}
    b = {}
    reta = {}
    print(f'\nReta {i + 1}:')
    ax = float(input('− Coordenada X de A: '))
    ay = float(input('− Coordenada Y de A: '))
    bx = float(input('− Coordenada X de B: '))
    by = float(input('− Coordenada Y de B: '))
    a['x'] = ax
    a['y'] = ay
    b['x'] = bx
    b['y'] = by
    reta['pontoA'] = a
    reta['pontoB'] = b
    retas.append(reta)
print('\nMedidas das retas:')
for i in range(quant):
    comp = comprimento(retas[i])
    print(f"- Reta {i + 1}: {comp:.2f}")
