def pesq_prod(codigo, vetor):
    if codigo not in vetor:
        return -1
    indice = vetor.index(codigo)
    return indice


codProd = [68, 54, 39, 37, 76, 93]
desProd = ['Burrito', 'Bisteca', 'Guacamole', 'Água', 'Feijão', 'Pastel']
preUnit = [3.02, 25, 3.6, 46, 15.07, 3.85]

print('Cupom Fiscal - Escadabaixo')
cod = 1
total = 0
while cod != 0:
    cod = int(input('Código do produto: '))
    while cod not in codProd:
        if cod == 0:
            break
        print('*** Código inválido ***')
        cod = int(input('Código do produto: '))
    if cod == 0:
        break
    quant = int(input('    - Quantidade: '))
    ind = pesq_prod(cod, codProd)
    preco = preUnit[ind] * quant
    print(f'    - {desProd[pesq_prod(cod, codProd)]} * {quant} = {preco:.2f} ')
    total += preco
print(f'Valor total: {total:.2f}')