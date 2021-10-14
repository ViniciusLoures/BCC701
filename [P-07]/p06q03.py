# Vinicius Alves Loures França 20.1.1039

c1 = input('Digite o nome do candidato 1: ')
n1 = int(input('Digite o número do candidato 1: '))
c2 = input('Digite o nome do candidato 2: ')
n2 = int(input('Digite o número do candidato 2: '))
votos_c1 = 0
votos_c2 = 0
validos = 0
nulos = 0
eleitores = int(input('Digite a quantidade de eleitores: '))
while eleitores < 3:
    print('A quantidade de eleitores é inferior a 3')
    eleitores = int(input('Digite a quantidade de eleitores: '))
print()
print('## Votação Iniciada')
for c in range(0, eleitores):
    voto = int(input('Digite o número do candidato que você deseja votar: '))
    if voto == n1:
        votos_c1 += 1
        validos += 1
    elif voto == n2:
        votos_c2 += 1
        validos += 1
    else:
        nulos += 1
print('## Votação encerrada')
print()
porcentagem_valida = 100 / eleitores * validos
porcentagem_invalida = 100 / eleitores * nulos
if validos > 0:
    porcentagem_c1 = 100 / validos * votos_c1
    porcentagem_c2 = 100 / validos * votos_c2
else:
    porcentagem_c1 = 0
    porcentagem_c2 = 0
print(f'Votos válidos: {porcentagem_valida:.2f}% ({validos} votos)')
print(f'Votos inválidos: {porcentagem_invalida:.2f}% ({nulos} votos)')
print(f'Votos para {c1}: {porcentagem_c1:.2f}% ({votos_c1} votos)')
print(f'Votos para {c2}: {porcentagem_c2:.2f}% ({votos_c2} votos)')