n = int(raw_input('Entre com nuermo: '))
for k in range(2,n):
     while n % k == 0:
          print k
          n = n/k
