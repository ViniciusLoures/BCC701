anos = int(input('Anos de experiência: '))
linguas = int(input('Linguagens de programação: '))
projetos = int(input('Projetos: '))
if anos < 3 or linguas < 3 or projetos < 5:
    print('Concorrendo à Vaga Júnior. Para concorrer à Vaga Pleno, faltam: ')
    FaltamAnos = 3 - anos
    FaltamLinguas = 3 - linguas
    FaltamProjetos = 5 - projetos
    if FaltamAnos > 0:
        print(f'− {FaltamAnos} anos de experiência')
    if FaltamLinguas > 0:
        print(f'− {FaltamLinguas} linguagens de programação')
    if FaltamProjetos > 0:
        print(f'- {FaltamProjetos} projetos')
elif anos >= 10 and linguas >= 5 and projetos >= 10:
    print('Concorrendo à Vaga Sênior')
elif anos >= 3 and linguas >= 3 and projetos >= 5:
    print('Concorrendo à Vaga Pleno. Para concorrer à Vaga Sênior, faltam: ')
    FaltamAnos = 10 - anos
    FaltamLinguas = 5 - linguas
    FaltamProjetos = 10 - projetos
    if FaltamAnos > 0:
        print(f'− {FaltamAnos} anos de experiência')
    if FaltamLinguas > 0:
        print(f'− {FaltamLinguas} linguagens de programação')
    if FaltamProjetos > 0:
        print(f'- {FaltamProjetos} projetos')
