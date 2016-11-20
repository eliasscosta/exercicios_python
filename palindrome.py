palavra = raw_input('Palavra: ')
if palavra == palavra[::-1]:
     print '%s e palindrome' %palavra
else:
     print '%s nao e palindrome' %palavra
