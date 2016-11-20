n = 1
maior = 0

while n <= 3:
     num = int(raw_input('Entre com o numero (%d)' %n))
     n = n + 1
     if num > maior:
          maior = num
print 'O maior e %d' %maior
