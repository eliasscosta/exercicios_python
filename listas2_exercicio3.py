peso = float(raw_input('Entre com o peso: '))
execesso = 0
taxa = 4
multa = 0
if peso > 50:
     execesso = peso - 50
     multa = execesso * taxa
print 'Peso do peixe: %5.2f\nPeso em execesso: %5.2f\nMulta foi de R$%5.2f' % (peso, execesso, multa)
