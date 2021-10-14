# Vinicius Alves Loures França 20.1.1039

def preencherVetor(valores, tipo):
    vetor = []
    valores = valores.split(',')
    for i in range(len(valores)):
        if tipo == 'int':
            valor = int(valores[i].strip())
        elif tipo == 'float':
            valor = float(valores[i].strip())
        else:
            valor = valores[i].strip()
        vetor.append(valor)
    return vetor


def contabilizarDemandas(idades):
    vetor85 = []
    vetor65 = []
    vetor45 = []
    vetor18 = []
    for i in range(len(idades)):
        if idades[i] >= 85:
            vetor85.append(idades[i])
        elif 85 > idades[i] >= 65:
            vetor65.append(idades[i])
        elif 65 > idades[i] >= 45:
            vetor45.append(idades[i])
        elif 45 > idades[i] >= 18:
            vetor18.append(idades[i])
    return len(vetor85), len(vetor65), len(vetor45), len(vetor18)


def criarVetor(qtdElementos, valorPadrao):
    vetor = []
    for i in range(qtdElementos):
        vetor.append(valorPadrao)
    return vetor


def avaliaAtendimento(vetor_demanda, vetor_vacina):
    indicador = 0
    for i in range(0, 4):
        if vetor_demanda[i] > vetor_vacina[i]:
            indicador += 1
    if indicador == 0:
        return True
    else:
        return False


idade = input('Defina as idades dos habitantes: ')
vetor_pessoas = preencherVetor(idade, 'int')
x85, x65, x45, x18 = contabilizarDemandas(vetor_pessoas)
print('Demandas a serem atendidas por faixa etária:')
print(f'. >= 85.........: {x85}')
print(f'.  < 85 e >= 65.: {x65}')
print(f'.  < 65 e >= 45.: {x45}')
print(f'. >= 18.........: {x18}')
vetor_demanda = [x85, x65, x45, x18]
vacina = input('Defina as disponibilidades de vacinas: ')
vetor_vacina = preencherVetor(vacina, 'int')
referencia = avaliaAtendimento(vetor_demanda, vetor_vacina)
if not referencia:
    print('Infelizmente, precisaremos de mais vacinas.')
else:
    print('A quantidade de vacinas é suficiente.')