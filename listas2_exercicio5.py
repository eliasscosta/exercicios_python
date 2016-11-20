n = 1
maior = 0
while n <= 3:
     num = int(raw_input('Entre com o numero (%d): ' %n))
     if n == 1:
          menor = num
     if num > maior:
          maior = num
     if num < menor:
          menor = num
     n = n + 1
print 'O maior e %d\nO menor e %d' %(maior,menor)
