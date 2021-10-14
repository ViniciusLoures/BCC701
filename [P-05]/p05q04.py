# Vinicius Alves Loures França 20.1.1039
num = int(input('Digite um número: '))
while num > 0:
    soma = 0
    for c in range(1, num - 1):
        if num % c == 0:
            soma += c
    if soma == num:
        print(f'{num} == {soma}: número é perfeito')
    else:
        print(f'{num} <> {soma}: número não é perfeito')
    num = int(input('Digite um número: '))
