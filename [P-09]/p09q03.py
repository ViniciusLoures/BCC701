# Vinicius Alves Loures França 20.1.1039

def primo(x):
    soma = 0
    for c in range(1, x + 1):
        if x % c == 0:
            soma += 1
    if soma == 2:
        return True
    else:
        return False


def check_primo(x, y):
    lista_primo = []
    for c in range(x, y + 1):
        if primo(c):
            lista_primo.append(c)
    return lista_primo


a = int(input('a: '))
while a <= 1:
    a = int(input('a: '))
b = int(input('b: '))
while b < a:
    b = int(input('b: '))
if a != b:
    lista = check_primo(a, b)
    print(f'Números primos entre {a} e {b}:')
    for i in range(len(lista)):
        print(lista[i], end=' ')
else:
    print(f'Números primos entre {a} e {b}:')
    if primo(a):
        print(a)