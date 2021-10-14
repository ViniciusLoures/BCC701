def fat4(inteiroPositivo):
    resp = 1
    for c in range(inteiroPositivo, 0, -4):
        resp *= c
    return resp


def combinacao4simples(n, p):
    c4 = fat4(n) / (fat4(p) * fat4(n - p))
    return c4


print('4-Fatorial e Combinação 4-simples')
n = int(input('Defina n: '))
while n <= 0:
    n = int(input('Erro na entrada. Defina n: '))
p = int(input('Defina p: '))
while p <= 0 or p > n:
    p = int(input('Erro na entrada. Defina p: '))
c4 = combinacao4simples(n, p)
print(f'C4({n},{p}) = {c4:.2f}')




