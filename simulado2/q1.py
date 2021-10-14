def dfat(inteiroPositivo):
    resp = 1
    if inteiroPositivo % 2 != 0:
        for i in range(1, inteiroPositivo + 1, 2):
            resp *= i
    else:
        for i in range(2, inteiroPositivo + 1, 2):
            resp *= i
    return resp


print('Fatorial Duplo')
entrada = int(input('Digite um número inteiro positivo: '))
while entrada < 0:
    print('Valor inválido !')
    entrada = int(input('Digite um número inteiro positivo: '))
saida = dfat(entrada)
print(f'{entrada}!! = {saida}')