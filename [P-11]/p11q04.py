# Vinicius Alves Loures França 20.1.1039

def preencherMatriz(string, tipo):
    matriz = []
    linhas = string.split(';')
    for lin in range(len(linhas)):
        linha = preencherVetor(linhas[lin],tipo)
        matriz.append(linha)
    return matriz


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


def calculaConsumos(vetorCapacidade, matrizQuilometragem):
    kmLitroVetor = []
    kmLitroMatriz = []
    for i in range(len(matrizQuilometragem)):
        for c in range(len(matrizQuilometragem[0])):
            kmLitroVetor.append(matrizQuilometragem[i][c] / vetorCapacidade[c])
        kmLitroMatriz.append(kmLitroVetor)
        kmLitroVetor = []
    return kmLitroMatriz


def imprimeVetor(vetor):
    print('[',end='')
    if len(vetor)>0:
        print(f'{vetor[0]:.2f}', end=' ')
        for i in range(1,len(vetor)):
            print(f', {vetor[i]:.2f}', end=' ')
    print(']', end='')


def imprimeMatriz(matriz):
    print(end='')
    if len(matriz) > 0:
        imprimeVetor(matriz[0])
    for lin in range(1, len(matriz)):
        print('\n', end='')
        imprimeVetor(matriz[lin])
    print(end='')


def calculaMedias(matrizConsumo):
    mediaConsumo = []
    for i in range(len(matrizConsumo[0])):
        mediaConsumo.append(0)
    for c in range(len(matrizConsumo)):
        for x in range(len(matrizConsumo[c])):
            mediaConsumo[x] += matrizConsumo[c][x]
    for y in range(len(mediaConsumo)):
        mediaConsumo[y] /= len(matrizConsumo)
    return mediaConsumo


print('Teste de consumo')
print('Capacidade dos tanques:')
capacidadeInput = input('>>> ')
if capacidadeInput == '':
    print('É necessário pelo menos um automóvel')
else:
    print('Quilometragens dos condutores:')
    quilometragemInput = input('>>> ')
    if quilometragemInput == '':
        print('Deve haver pelo menos um condutor')
    else:
        capacidadeVetor = preencherVetor(capacidadeInput, 'int')
        quilometragemMatriz = preencherMatriz(quilometragemInput, 'int')
        if len(capacidadeVetor) != len(quilometragemMatriz[0]):
            print('Quantidade de automóveis incompatível')
        else:
            consumo = calculaConsumos(capacidadeVetor, quilometragemMatriz)
            print('Consumos km/l:')
            imprimeMatriz(consumo)
            print('')
            mediaConsumo = calculaMedias(consumo)
            print('Médias dos consumos por automóvel:')
            imprimeVetor(mediaConsumo)