l = float(input('Forneça o comprimerto do fio: '))
p = float(input('Forneça a força peso: '))
m = float(input('Forneça a massa: '))
g = p / m
t = 2 * 3.14 * ((l / g)**0.5)
print('A aceleração da gravidade é {:.3f}'.format(g))
print('O período do pêndulo é {:.3f}'.format(t))