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
    print(" ]")


vetorV = [8, 9, 9, 4]
vetorN = ['Fluminense', 'Santos', 'Internacional', 'Atlético-MG']
print('Apuração tntsports.com.br')
print(f'Vetor N:')
imprimeVetor(vetorN)
print(f'Vetor V:')
imprimeVetor(vetorV)
matrizM = input('Entrada da matriz M:\n>>> ')
matrizM = preencherMatriz(matrizM, 'int')
flu = santos = inter = menordeminas = 0
for i in range(len(matrizM[0])):
    flu += matrizM[0][i]
    santos += matrizM[1][i]
    inter += matrizM[2][i]
    menordeminas += matrizM[3][i]
print('Clubes com pontuação correta:')
cont = 0
if flu == vetorV[0]:
    print(' - Fluminense')
    cont += 1
if santos == vetorV[1]:
    print(' - Santos')
    cont += 1
if inter == vetorV[2]:
    print(' - Fluminese')
    cont += 1
if menordeminas == vetorV[3]:
    print(' - Atlético-MG')
    cont += 1
print(f'Porcentagem de acertividade: {cont * 25}.0%')