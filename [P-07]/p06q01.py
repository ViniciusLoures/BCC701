# Vinicius Alves Loures França 20.1.1039

n = int(input('Número de termos: '))
r = int(input('Raio da esfera: '))
pi = 0
for i in range(0, n):
    pi += ((-1) ** i) * (4 / (2 * i + 1))
print(f'pi = {pi:.10f}.')
v = 4 / 3 * pi * r ** 3
print(f'Volume da esfera = {v:.10f}.')