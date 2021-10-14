# Vinicius Alves Loures França 20.1.1039
from math import inf


def preencherMatriz(valores, tipo):
    matriz = []
    linhas = valores.split(';')
    for lin in range(len(linhas)):
        colunas = linhas[lin].split(',')
        vetor = []
        for col in range(len(colunas)):
            if tipo == 'int':
                valor = int(colunas[col].strip())
            elif tipo == 'float':
                valor = float(colunas[col].strip())
            else:
                valor = colunas[col].strip()
            vetor.append(valor)
        matriz.append(vetor)
    return matriz


def linhaMenorValor(matriz):
    lineMenorValor = 0
    menorValor = inf
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[i][c] < menorValor:
                menorValor = matriz[i][c]
                lineMenorValor = i
    return lineMenorValor


def colunaMaiorValor(matriz, indice):
    lineMenorValor = matriz[indice]
    maiorValor = 0
    for i in range(len(lineMenorValor)):
        if i == 0:
            maiorValor = lineMenorValor[i]
        elif maiorValor < lineMenorValor[i]:
            maiorValor = lineMenorValor[i]
    indiceMaiorValor = lineMenorValor.index(maiorValor)
    return indiceMaiorValor


print('MinMax de uma Matriz')
print('Valores da matriz:')
matrizInput = input('>>> ')
matriz = preencherMatriz(matrizInput, 'int')
a = linhaMenorValor(matriz)
b = colunaMaiorValor(matriz, a)
print(f'MinMax: [{a}, {b}] = {matriz[a][b]}')
