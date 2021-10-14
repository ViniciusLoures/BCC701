def fun_dividendo(valorK):
    dividendo = 9 ** valorK
    return dividendo


def fun_divisor(valorK):
    divisor = (4 * valorK) + 1
    return divisor


print('Resultados para W')
quant_M = int(input('Quantidade de termos M: '))
resposta = 0
while 45 > quant_M > 9:
    for i in range(quant_M):
        resposta += fun_dividendo(i) / fun_divisor(i)
    print(f'Força imaginária W = {resposta}')
    quant_M = int(input('Quantidade de termos M: '))