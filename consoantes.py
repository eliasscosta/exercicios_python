soma = 0
i = 1
vetor = []
while i <= 10:
     letra = raw_input('Entre com o caracter: ')
     vetor.append(letra)
     if letra.lower() not in 'aeiou':
          soma += 1
     i += 1
print 'Foi digitado %d consoantes' % soma 
