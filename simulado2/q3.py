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


def imprimeVetor(vetor):
    print('[', end='')
    if len(vetor) > 0:
        print(f' {vetor[0]}', end='')
        for c in range(1, len(vetor)):
            print(f', {vetor[i]}', end='')
    print(' ]', end='')


def imprimeMatriz(matriz):
    if len(matriz) > 0:
        imprimeVetor(matriz[0])
        print('')
        for lin in range(1, len(matriz)):
            imprimeVetor(matriz[lin])
            print('')


print('Loja da tia Maria')
estoque = input('Matriz de estoque: ')
matrizEstoque = preencherMatriz(estoque, 'int')
att = int(input('Número de atualizações:'))
for i in range(0, att):
    loja = int(input('Índice da loja: '))
    produto = int(input('Índice do produto: '))
    novoEstoque = int(input('Novo estoque:'))
    matrizEstoque[loja][produto] = novoEstoque
    imprimeMatriz(matrizEstoque)
