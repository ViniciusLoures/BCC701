# Vinicius Alves Loures França 20.1.1039
years = int(input('Anos de experiência: '))
language = int(input('Linguagens de programação: '))
projects = int(input('Projetos: '))
diff_years = 3 - years
diff_language = 3 - language
diff_projects = 5 - projects
diff_years_senior = 10 - years
diff_language_senior = 5 - language
diff_projects_senior = 10 - projects
if years < 3 or language < 3 or projects < 5:
    print('Concorrendo à Vaga Júnior. Para concorrer à Vaga Pleno, faltam: ')
    if diff_years > 0:
        print(f'− {diff_years} anos de experiência')
    if diff_language > 0:
        print(f'− {diff_language} linguagens de programação')
    if diff_projects > 0:
        print(f'- {diff_projects} projetos')
elif years >= 10 and language >= 5 and projects >= 10:
    print('Concorrendo à Vaga Sênior')
elif years >= 3 and language >= 3 and projects >= 5:
    print('Concorrendo à Vaga Pleno. Para concorrer à Vaga Sênior, faltam: ')
    if diff_years_senior > 0:
        print(f'− {diff_years_senior} anos de experiência')
    if diff_language_senior > 0:
        print(f'− {diff_language_senior} linguagens de programação')
    if diff_projects_senior > 0:
        print(f'- {diff_projects_senior} projetos')
