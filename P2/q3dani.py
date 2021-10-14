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


print('Secretarias Municipais de Saúde')
verbasEntrada = input('Valores iniciais: ')
verbasMatriz = preencherMatriz(verbasEntrada, 'int')
cidade = 1
while cidade >= 0:
    cidade = int(input('Índice da cidade: '))
    if cidade < 0:
        print('Matriz final: ')
        imprimeMatriz(verbasMatriz)
    else:
        estado = int(input('Índice do estado: '))
        print(f'Valor atual: {verbasMatriz[cidade][estado]}')
        novo = int(input('Novo valor: '))
        print(f'Diferença: {verbasMatriz[cidade][estado] - novo}')
        verbasMatriz[cidade][estado] = novo