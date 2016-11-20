messes = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
dia, mes, ano = raw_input('Entre com a data (DD/MM/AAAA): ').split('/')

print 'Voce nascem em: '
print '%s de %s de %s' %(dia, messes[int(mes) -1], ano)
