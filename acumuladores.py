n = 1
soma = 0
while n <= 10:
     x = int(raw_input('Digite o numero %d: ' % n))
     soma = soma + x
     n = n + 1
print 'Soma: %5.2f' %(soma/10)
