def preencherMatriz(valores, tipo):
    matriz = []
    linhas = valores.split(";")
    for lin in range(len(linhas)):
        colunas = linhas[lin].split(",")
        vetor = []
        for col in range(len(colunas)):
            if tipo == "int":
                valor = int(colunas[col].strip())
            elif tipo == "float":
                valor = float(colunas[col].strip())
            else:
                valor = colunas[col].strip()
            vetor.append(valor)
        matriz.append(vetor)
    return matriz


def imprimeVetor(vetor):
    print("[", end="")
    if len(vetor) > 0:
        print(f" {vetor[0]}", end="")
        for i in range(1, len(vetor)):
            print(f", {vetor[i]}", end="")
    print(" ]", end="")


def imprimeMatriz(matriz):
    if len(matriz) > 0:
        imprimeVetor(matriz[0])
        print("")
        for lin in range(1, len(matriz)):
            imprimeVetor(matriz[lin])
            print("")


print('Medições SANEOURO')
matriz = input('Valores iniciais: ')
matriz = preencherMatriz(matriz, 'float')
while True:
    predio = int(input('Índice do prédio: '))
    if predio < 0:
        break
    apartamento = int(input('Índice do apartamento: '))
    print(f'Valor atual: {matriz[predio][apartamento]}')
    novo = float(input('Novo valor: '))
    print(f'Diferença: {matriz[predio][apartamento] - novo}')
    matriz[predio][apartamento] = novo
print('Valores finais: ')
imprimeMatriz(matriz)