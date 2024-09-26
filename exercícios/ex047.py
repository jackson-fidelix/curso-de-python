#impressão de números pares de 1 à 50
contador_pares = 0
for c in range(2, 50+1, 2):
    if c % 2 == 0:
        print(c, end=" ")
        contador_pares +=  1
print('Fim da apresentação dos números pares.')
print('Existem {} números pares de 1 à 50.'.format(contador_pares))