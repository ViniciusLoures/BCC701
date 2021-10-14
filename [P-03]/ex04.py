peso = float(input('Digite seu peso (em kg): '))
altura = float(input('Digite sua altura (em metros): '))
sexo = input(f'Seu sexo é masculino (M) ou feminino (F)? ')
imc = peso / altura ** 2
if sexo == 'M':
    if imc > 25:
        x = 25 * (peso ** 2)
        y = peso - x
        print(f'Você deve perder {y:.2f} KG para ter IMC = 25')
    else:
        print('Você não precisa perder peso para ter IMC <= 25')
if sexo == 'F':
    if imc > 24:
        x = 24 * (peso ** 2)
        y = peso - x
        print(f'Você deve perder {y:.2f} KG para ter IMC = 24')
    else:
        print('Você não precisa perder peso para ter IMC <= 24')
if sexo not in 'FM':
    print('A entrada contém dados não reconhecidos')