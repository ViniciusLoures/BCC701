# Vinicius Alves Loures França 20.1.1039
weight = float(input('Informe o peso:  '))
height = float(input('Informe a altura: '))
imc = weight / (height ** 2)
print(f'Seu IMC é {imc:.2f}')
if imc < 20:
    print('IMC abaixo do normal.')
elif imc <= 25:
    print('IMC normal')
elif imc < 30:
    print('IMC indica sobrepeso')
elif imc < 40:
    print('IMC indica obesidade leve a moderada')
else:
    print('IMC indica obesidade mórbida')
