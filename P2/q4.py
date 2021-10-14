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



def funcao(vetor, matriz):


print('Organização das nações ')
pli = [67, 12, 74, 25, 30, 52]
matriz = input('Valores da matriz: ')
matriz = preencherMatriz(matriz, 'int')
if len(matriz) != 6 or len(matriz[0]) != 4:
    print('Entrada invalida')
else:
    for i in range(len(matriz)):
