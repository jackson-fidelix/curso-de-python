from math import hypot
cat_oposto = float(input('Comprimento do Cateto Oposto: '))
cat_adjacente = float(input('Comprimento do Cateto Adjacente: '))
hipot = hypot(cat_oposto, cat_adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipot))
