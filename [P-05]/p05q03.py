# Vinicius Alves Loures França 20.1.1039
t = float(input('Capital Total para empréstimo: '))
while True:
    c = float(input('Capital emprestado: '))
    if t < c:
        print(f'Empréstimo negado, capital total é de R$ {t:.2f}.')
        break
    t -= c
    m = int(input('Quantidade de meses para quitação: '))
    if c <= 10000:
        print('Taxa de juros aplicada: 10%.')
        j = c * 0.1 * m
        print(f'Juros devido: {j:.2f}.')
        print(f'Valor total: {j + c:.2f}.')
    else:
        print('Taxa de juros aplicada: 7%.')
        j = c * 0.07 * m
        print(f'Juros devido: {j:.2f}.')
        print(f'Valor total: {j + c:.2f}.')
