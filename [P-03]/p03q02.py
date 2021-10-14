average_14 = float(input('Média móvel dos últimos 14 dias: '))
average_6 = int(input('Somatório dos casos dos últimos 6 dias: '))
today = int(input('Quantidade de casos de hoje: '))
average_7 = (average_6 + today) / 7
diff = average_7 - average_14
growth_rate = diff / average_14 * 100
if growth_rate < 0:
    growth_rate = growth_rate * (-1)
    print(f'Casos diminuindo em {growth_rate:.2f}%')
elif growth_rate <= 15:
    print(f'Casos estáveis em {growth_rate:.2f}%')
else:
    print(f'Casos aumentando em {growth_rate:.2f}%')
