# Vinicius Alves Loures França 20.1.1039

name = input('Informe o nome do juiz: ')
quant = int(input('Quantidade de partidas: '))
impedimentos = 0
faltas = 0
cartao = 0
tempo = 0
print()
for c in range(1, quant+1):
    print(f'Partida {c}:')
    impedimentos += int(input('. Impedimentos.......: '))
    faltas += int(input('. Faltas.............: '))
    cartao += int(input('. Cartões............: '))
    tempo += float(input('. Tempo de acréscimo.: '))
    print()
print(f'Estatísticas do juiz {name}')
print(f'. Impedimentos.......: {impedimentos/quant:.2f}.')
print(f'. Faltas.............: {faltas/quant:.2f}.')
print(f'. Cartões............: {cartao/quant:.2f}.')
print(f'. Tempo de acréscimo.: {tempo/quant:.2f}.')
