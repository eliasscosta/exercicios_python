n = 1
fat = 1
num = int(raw_input('Digite num: '))
while n <= num:
     fat = fat * n
     n = n + 1
print 'Fatorial(%d): %d' % (num, fat)
