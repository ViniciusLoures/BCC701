# Vinicius Alves Loures França 20.1.1039

flag = input('Deseja imprimir um retângulo? (s/n) ')
while True:
    if flag in 'Nn':
        quit()
    h = int(input('Altura do retângulo: '))
    l = int(input('Largura do retângulo: '))
    while l < h or l <= 0 or h <= 0:
        print('Valor inválido.')
        print()
        h = int(input('Altura do retângulo: '))
        l = int(input('Largura do retângulo: '))
    print()
    for c in range(0, h):
        print('*' * l)
    print()
    flag = input('Deseja imprimir outro retângulo? (s/n) ')
