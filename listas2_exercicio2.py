ano = int ( raw_input("Entre com o ano: "))
if ano % 400 == 0:
     print 'Ano bisexto %d' %ano 
elif ano % 100 != 0 and ano % 4 == 0:
     print 'Ano bisexto %d' %ano 
else:
     print 'Ano nao bisexto %d' %ano
