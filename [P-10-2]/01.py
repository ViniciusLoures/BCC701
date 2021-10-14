def preencherVetor(valores, tipo):
    vetor = []
    valores = valores.split(',')
    for i in range(len(valores)):
        if tipo == 'int':
            valor = int(valores[i].strip())
        elif tipo == 'float':
            valor = float(valores[i].strip())
        else:
            valor = valores[i].strip()
        vetor.append(valor)
    return vetor


def calculaLucros(coxas, lucros_coxas, quibes, lucro_quibes):
    lucro = []
    for i in range(len(coxas)):
        x = (coxas[i] * lucros_coxas) + (quibes[i] * lucro_quibes)
        lucro.append(x)
    return lucro


def imprimeVetor(vetor):
    print('[ ', end='')
    if len(vetor) > 0:
        print(f'{vetor[0]:.2f}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]:.2f}', end='')
    print(' ]')


coxas = input('Vendas de coxinhas: ')
quant_coxas = preencherVetor(coxas, 'float')
quibes = input('Vendas de quibes: ')
quant_quibes = preencherVetor(quibes, 'float')
if len(quant_coxas) != len(quant_quibes):
    print('Dados de vendas inválidos')
    quit()
lucro_coxas = float(input('Lucro por unidade de coxinha: R$ '))
lucro_quibes = float(input('Lucro por unidade de quibe: R$ '))
lucro_final = calculaLucros(quant_coxas, lucro_coxas, quant_quibes, lucro_quibes)
print(f'Lucros: {imprimeVetor(lucro_final)}')
print(f'Maior lucro: R$ {max(lucro_final):.2f}')
print(f'Menos lucro: R$ {min(lucro_final):.2f}')