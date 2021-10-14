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


print('Manipulações de valores de Vetor')
vetorX = input('Vetor X: ')
vetorX = preencherVetor(vetorX, 'float')
quantElementos = len(vetorX)
maior, menor, media = analisaVetor(vetorX)
print('Propriedades do vetor X: ')
print(f'- Possui {quantElementos} elementos')
print(f'- {menor:.2f} é o menor valor')
print(f'- {maior:.2f} é o maior valor')
print(f'- A média dos valores é {media:.2f}')
