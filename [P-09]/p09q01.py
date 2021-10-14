# Vinicius Alves Loures França 20.1.1039

def SomarPar(x, y):
    lista_par = []
    soma_par = 0
    for c in range(x, y + 1):
        if c % 2 == 0:
            lista_par.append(c)
    for n in lista_par:
        soma_par += n
    return soma_par


def SomarImpar(x, y):
    lista_impar = []
    soma_impar = 0
    for c in range(x, y + 1):
        if c % 2 != 0:
            lista_impar.append(c)
    for n2 in lista_impar:
        soma_impar += n2
    return soma_impar


n1 = int(input('N1: '))
n2 = int(input('N2: '))
while n2 < n1:
    n2 = int(input('N2: '))
soma_par = SomarPar(n1, n2)
soma_impar = SomarImpar(n1, n2)
print(f'Somatório de números pares em [{n1}, {n2}]: {soma_par}')
print(f'Somatório de números impares em [{n1}, {n2}]: {soma_impar}')
