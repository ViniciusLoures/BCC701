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


def comparaVetores(morte_anterior, morte_atual):
    dados = []
    for i in range(len(morte_atual)):
        if morte_anterior[i] > morte_atual[i]:
            dados.append('R')
        elif morte_anterior[i] < morte_atual[i]:
            dados.append('A')
        else:
            dados.append('E')
    return dados


def imprimeVetor(vetor):
    print('[ ', end='')
    if len(vetor) > 0:
        print(f'{vetor[0]}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]}', end='')
    print(' ]')


def classificaEstado(dados):
    if dados.count('R') < dados.count('A'):
        return 'Onda Vermelha'
    elif dados.count('R') > dados.count('A'):
        return 'Onda Verde'
    elif dados.count('R') == dados.count('A'):
        return 'Onda Amarela'


anterior = input('Número de mortes na semana anterior: ')
atual = input('Número de mortes na semana atual: ')
morte_anterior = preencherVetor(anterior, 'int')
morte_atual = preencherVetor(atual, 'int')
if len(morte_atual) != len(morte_anterior):
    print(f'Número de elementos incompatível ({len(morte_anterior)} != {len(morte_atual)})')
    quit()
dados = comparaVetores(morte_anterior, morte_atual)
print('Classificações das macro-regiões:')
imprimeVetor(dados)
print(f'Classificação do estado: {classificaEstado(dados)}')