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


vetorV = [41, 55, 91, 18, 8, 75]
print('Desafio - Netflix')
matrizM = input('Matriz M: ')
preencherMatriz(matrizM, 'int')
for i in range(len(matrizM)):
    for c in range(len(matrizM[0])):
        if 41 == matrizM[c]:
            coluna = 
        print(primeiro)