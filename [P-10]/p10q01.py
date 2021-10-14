# Vinicius Alves Loures França 20.1.1039

def preencherVetor(valores, tipo):
    vetor = []
    valores = valores.split(',')
    for i in range(0, len(valores)):
        if tipo == 'int':
            valor = int(valores[i].strip())
        elif tipo == 'float':
            valor = float(valores[i].strip())
        else:
            valor = valores[i].strip()
        vetor.append(valor)
    return vetor


def estatNotas(vetor):
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


notas = input('Notas: ')
a = preencherVetor(notas, 'float')
mai, men, med = estatNotas(a)
print(f'Maior nota: {mai:.1f}')
print(f'Menor nota: {men:.1f}')
print(f'Nota média: {med:.1f}')