min = int (raw_input('Entre com valtor de minutos:'))
if min < 200:
     preco = 0.20
elif min <= 400:
     preco = 0.18
elif min <= 800:
     preco = 0.15
else:
     preco = 0.08
print 'O valor da sua fatura e R$', min*preco 

     
