average = float(input('Média no semestre: '))
absence = int(input('Frequência no semestre: '))
diff_average = 6 - average
diff_absence = 75 - absence
if average >= 6 and absence >= 75:
    print(f'Conceito: aprovado')
if average < 6 and absence >= 75:
    print(f'Conceito: exame especial')
    print(f'Justificativa: média {diff_average:.2f} abaixo da mínima')
if absence < 75:
    print(f'Conceito: reprovado por faltas')
    print(f'Justificativa: frequência {diff_absence}% abaixo da mínima')
