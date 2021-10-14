weight = float(input('Digite seu peso (em kg): '))
height = float(input('Digite sua altura (em metros): '))
genre = input(f'Seu sexo é masculino (M) ou feminino (F)? ')
imc = weight / (height ** 2)
if genre in 'Mm':
    if imc > 25:
        ideal_weight = 25 * (height ** 2)
        diff = weight - ideal_weight
        print(f'Você deve perder {diff:.2f} KG para ter IMC = 25')
    else:
        print('Você não precisa perder peso para ter IMC <= 25')
if genre in 'Ff':
    if imc > 24:
        ideal_weight = 24 * (height ** 2)
        diff = weight - ideal_weight
        print(f'Você deve perder {diff:.2f} KG para ter IMC = 24')
    else:
        print('Você não precisa perder peso para ter IMC <= 24')
if genre not in 'FfMm':
    print('A entrada contém dados não reconhecidos')
