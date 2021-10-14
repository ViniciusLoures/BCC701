from math import sqrt


def preencherVetor(valores, tipo):
    vetor = []
    valores = valores.split(",")
    for i in range(len(valores)):
        if tipo == "int":
            valor = int(valores[i].strip())
        elif tipo == "float":
            valor = float(valores[i].strip())
        else:
            valor = valores[i].strip()
        vetor.append(valor)
    return vetor


def media3ponderada(vetor):
    resp = 0
    for c in range(len(vetor)):
        resp += vetor[c] * 3**c
    resp = resp / (3**len(vetor) - 1)
    return resp


def mediaQuadratica(vetor):
    resp = 0
    for c in range(len(vetor)):
        resp += vetor[c]**2
    resp = resp / len(vetor)
    resp = sqrt(resp)
    return resp


def analisaVetor(vetor):
    maior = 0
    menor = 0
    media = 0
    for i in range(len(vetor)):
        if i == 0:
            maior = menor = vetor[i]
        else:
            if vetor[i] > maior:
                maior = vetor[i]
            if vetor[i] < menor:
                menor = vetor[i]
        media += vetor[i]
    media = media/len(vetor)
    return maior, menor, media


print('Calculando Médias')
vetorV = input('Elementos de V: ')
vetorV = preencherVetor(vetorV, 'float')
ponderada = media3ponderada(vetorV)
quadrada = mediaQuadratica(vetorV)
print(f'Média Quadrática = {quadrada:.2f}')
print(f'Média 3-ponderada = {ponderada:.2f}')
print(f'Média Quadrática + Média 3-ponderada = {ponderada + quadrada:.2f}')
