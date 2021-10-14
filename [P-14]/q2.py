# Vinicius Alves Loures França 20.1.1039
quant_alunos = int(input('Quantidade de alunos: '))
quant_discip = int(input('Quantidade de disciplinas: '))
alunos = []

for i in range(quant_alunos):
    rep = []
    print(f'\nDados do aluno {i + 1}:')
    for c in range(quant_discip):
        aluno = {}
        print(f'− Dados da disciplina {c + 1}:')
        aluno['nota'] = float(input('− Nota: '))
        aluno['frequencia'] = int(input('− Frequência: '))
        rep.append(aluno)
    alunos.append(rep)
print('\nMaiores notas e frenquências: ')
maior_nota = -1
maior_freq = -1
for i in range(quant_alunos):
    for c in range(quant_discip):
        if i and c == 0:
            maior_nota = alunos[i][c]['nota']
            maior_freq = alunos[i][c]['frequencia']
        elif alunos[i][c]["nota"] > maior_nota:
            maior_nota = alunos[i][c]['nota']
        if alunos[i][c]["frequencia"] > maior_freq:
            maior_freq = alunos[i][c]['frequencia']
    print(f'- Aluno {i + 1}: nota = {maior_nota}; frequência = {maior_freq}')
