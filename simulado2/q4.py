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


print('Ministério do Meio Ambiente')
metas = input('Metas dos estados: ')
metas = preencherVetor(metas, 'int')
plantio = input('Plantio de árvores: ')
plantio = preencherMatriz(plantio, 'int')
total = 0
for x in range(len(metas)):
    for y in range(len(plantio)):
        total += plantio[y][x]
    if total < metas[x]:
        print(f'Estado {x + 1}, meta = {metas[x]}, plantio = {total}')
    total = 0
