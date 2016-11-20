valor_hora = float(raw_input('Entre com o valor da sua hora: '))
qtd_hora = float(raw_input('Entre com o a qtd de hora trabalhada/mes: '))
salario = valor_hora*qtd_hora
print '+ Salario Bruto: R$%5.2f' % (salario)
print '- IR (11): R$%5.2f' % (salario*0.11)
print '- INSS (8): R$%5.2f' % (salario*0.08)
print '- Sindicato (5): R$%5.2f' % (salario*0.05)
print 'Salario Liquido: R$%5.2f' % float(salario-(salario*0.11)-(salario*0.08)-(salario*0.05))
