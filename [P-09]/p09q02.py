# Vinicius Alves Loures França 20.1.1039

def fatorial(x):
    fat = 1
    for i in range(2, x + 1):
        fat = fat * i
    return fat


def euler(x):
    e = 0
    for i in range(x):
        e += 1 / fatorial(i)
    return e


while True:
    t = int(input('Defina T: '))
    if t <= 0:
        break
    e = euler(t)
    print(f'O número de Euler com {t} termos é {e:.5f}.')