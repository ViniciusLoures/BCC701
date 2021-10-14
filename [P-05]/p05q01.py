# Vinicius Alves Loures França 20.1.1039

comprimento = float(input('Comprimento de corte dos tubos: '))
margem_de_erro = float(input('Margem de erro aceitável: '))
quant = int(input('Quantidade de tubos demandada: '))
margem_mais = comprimento + margem_de_erro
margem_menos = comprimento - margem_de_erro
total = 0
rejeitados = 0
while True:
    corte = float(input('Comprimento do tudo cortado: '))
    total += 1
    if margem_menos <= corte <= margem_mais:
        quant -= 1
    else:
        print('Acima da margem de erro, tudo rejeitado')
        rejeitados += 1
    if quant == 0:
        break
print('Fim da produção, demanda atendida.')
print(f'Total de tubos cortados: {total}')
print(f'Total de tubos rejeitados: {rejeitados}')
