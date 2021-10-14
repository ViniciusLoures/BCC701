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


def notasAlunos(vetorGabarito, matrizNotas):
    nota = []
    for i in range(len(matrizNotas)):
        acertos = 0
        for c in range(len(matrizNotas[i])):
            if matrizNotas[i][c] == vetorGabarito[c]:
                acertos += 1
        nota.append((acertos*10)/len(vetorGabarito))
    return nota


def imprimeVetor(vetor):
    print('[ ', end='')
    if len(vetor) > 0:
        print(f'{vetor[0]:.2f}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]:.2f}', end='')
    print(' ]', end='')


print('Notas de BCC701')
print('Digite o gabarito:')
gabaritoInput = input('>>> ')
print('Digite as respostas dos alunos:')
notasInput = input('>>> ')
a = preencherVetor(gabaritoInput, 'str')
b = preencherMatriz(notasInput, 'str')
vetorNotas = notasAlunos(a, b)
if notasInput == '':
    print('Nenhum aluno para avaliar')
    quit()
elif len(b[0]) != len(a):
    print('Quantidade de questões incompatível')
    quit()
print('Notas dos alunos:')
imprimeVetor(vetorNotas)