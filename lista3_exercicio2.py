teste = False
while teste == False:
     nome = raw_input('Entre com o nome: ')
     senha = raw_input('Entre com a senha: ')
     if nome.upper() != senha.upper():
          teste = True
     else:
          teste = False
print 'Seu nome e %s e sua senha e %s' %(nome,senha)
