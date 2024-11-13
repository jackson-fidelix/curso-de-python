#Aula 16 sobre TUPLAS
#lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

#primeira forma de se fazer
#for comida in lanche:
#    print(f'Eu vou comer {comida}')

#segunda forma de se fazer
#for cont in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#terceira forma de se fazer
#for pos, comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}')

#isso ordena em ordem alfabética
#print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(8))
