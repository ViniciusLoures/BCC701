# Vinicius Alves Loures França 20.1.1039

def calculaF(x, y):
    r = (x ** 2) + (2 * x * y) + y
    return r


def calculaG(x, y):
    r = (y ** 2) + (2 * x * y) + x
    return r


a = int(input('a: '))
b = int(input('b: '))
p = int(input('p: '))

print(f'Intervalo definido: [ {a}, {b} ], com passo {p}.')
