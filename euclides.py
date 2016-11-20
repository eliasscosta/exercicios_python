a = int(raw_input('a: '))
b = int(raw_input('b: '))

while a % b != 0:
     a, b = b, a % b

print 'mdc = %d' % b
