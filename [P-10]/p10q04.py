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


def acimaMedia(vetor, corte):
    new_vetor = []
    for i in range(len(vetor)):
        if vetor[i] > corte:
            new_vetor.append(i)
    return new_vetor


def imprimeIndice(vetor):
    print('[ ', end='')
    if len(vetor) > 0:
        print(f'{vetor[0]}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]}', end='')
    print(' ]')


def imprimeVetor(vetor):
    print('[ ', end='')
    if len(vetor) > 0:
        print(f'{vetor[0]:.1f}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]:.1f}', end='')
    print(' ]')


def imprimeNomeNota(indice, nota, nome):
    print('[ ', end='')
    for i in range(len(indice)):
        if i == (len(indice) - 1):
            print(f'{nota[indice[i]]:.1f} ({nome[indice[i]]})', end=' ')
        else:
            print(f'{nota[indice[i]]:.1f} ({nome[indice[i]]})', end=', ')
    print(']')


def exameEspecial(lista):
    indiceExameEspecial = []
    for i in range(len(lista)):
        if 3 <= lista[i] < 6:
            indiceExameEspecial.append(i)
    return indiceExameEspecial


notas = input('Notas: ')
nomes = input('Nomes: ')
lista_notas = preencherVetor(notas, 'float')
lista_nomes = preencherVetor(nomes, 'str')
mai, men, med = estatNotas(lista_notas)
print(f'Maior nota: {mai:.1f}')
print(f'Menor nota: {men:.1f}')
print(f'Nota média: {med:.1f}')
indice = acimaMedia(lista_notas, med)
indice_exame = exameEspecial(lista_notas)
print(f'Índices das notas acima da média:')
imprimeIndice(indice)
print('Notas acima da média:')
lista_media = []
for c in range(len(indice)):
    lista_media.append([indice[c]])
lista_final = []
imprimeNomeNota(indice, lista_notas, lista_nomes)
print(f'Índices das notas para Exames Especiais:')
imprimeIndice(indice_exame)
print(f'Notas para Exames Especiais:')
imprimeNomeNota(indice_exame, lista_notas, lista_nomes)