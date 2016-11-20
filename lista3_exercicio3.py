hab_a = 80000
hab_b = 200000
taxa_a = 0.03
taxa_b = 0.015
n = 1
while True:
     hab_a = hab_a + (hab_a*taxa_a)
     hab_b = hab_b + (hab_b*taxa_b)
     #print 'PopA: %d\nPopB: %d' %(hab_a,hab_b)
     if hab_a >= hab_b:
          print 'Foi necessario %d anos para igualar!\nPopA: %d\nPopB: %d' %(n, hab_a,hab_b)
          break
     n = n +1
