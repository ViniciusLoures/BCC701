cash = float(input('Capital emprestado: '))
months = int(input('Quantidade de meses para quitação: '))
if cash <= 10000.00:
    rate = 0.10
    print('Taxa de juros aplicada: 10%')
else:
    rate = 0.07
    print('Taxa de juros aplicada: 7%')
rateT = cash * rate * months
total = rateT + cash
print(f'Juros devido: {rateT:.2f}')
print(f'Valor total: {total:.2f}')
