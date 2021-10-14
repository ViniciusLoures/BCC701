# Vinicius Alves Loures França 20.1.1039

from math import factorial
num = int(input('Informe o número que deseja calcular o Fatorial: '))
while True:
    if num < 1:
        num = int(input('Número inválido, defina outro: '))
    else:
        break
print(f'O Fatorial de {num} é: {factorial(num)}')
