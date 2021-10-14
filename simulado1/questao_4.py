apre = int(input('Defina a quantidade de apresentações: '))
juiz = int(input('Defina a quantidade de juízes: '))
total = 0
for i in range(1, apre + 1):
    print(f'. Apresentação {i}:')
    grau = float(input('. Grau de dificuldade: '))
    for x in range(1, juiz + 1):
        nota = float(input(f'. Nota do juíz {x}: '))
        total += nota
    print(f'. Pontuação da apresentação: {total * grau:.2f}')
    total = 0
