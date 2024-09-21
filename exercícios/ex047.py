#impressão de números pares de 1 à 50
contador_pares = 0
for c in range(1, 50+1, 1):
    if c % 2 == 0:
        print(c)
        contador_pares +=  1
print('Fim da apresentação dos números pares.')
print('Existem {} números pares de 1 à 50.'.format(contador_pares))