idade = int(input('Informe a idade: '))
if idade < 16:
    print('Idade inválida.')
    quit()
base = float(input('Informe o valor base: R$ '))
sexo = int(input('Informe o sexo: '))
estado = int(input('Informe o estado civil: '))
if sexo == 1:
    if estado == 1:
        if idade < 39:
            print('Percentual de acréscimo: 0.90%.')
            print(f'Valore final do seguro: R$ {base * 1.009:.2f}')
        else:
            print('Percentual de acréscimo: 1.70%.')
            print(f'Valore final do seguro: R$ {base * 1.017:.2f}')
    else:
        if idade < 39:
            print('Percentual de acréscimo: 1.30%.')
            print(f'Valore final do seguro: R$ {base * 1.013:.2f}')
        else:
            print('Percentual de acréscimo: 2.10%.')
            print(f'Valore final do seguro: R$ {base * 1.021:.2f}')
elif sexo == 2:
    if estado == 1:
        if idade < 39:
            print('Percentual de acréscimo: 1.20%.')
            print(f'Valore final do seguro: R$ {base * 1.012:.2f}')
        else:
            print('Percentual de acréscimo: 2.00%.')
            print(f'Valore final do seguro: R$ {base * 1.02:.2f}')
    else:
        if idade < 39:
            print('Percentual de acréscimo: 1.60%.')
            print(f'Valore final do seguro: R$ {base * 1.016:.2f}')
        else:
            print('Percentual de acréscimo: 2.40%.')
            print(f'Valore final do seguro: R$ {base * 1.024:.2f}')

