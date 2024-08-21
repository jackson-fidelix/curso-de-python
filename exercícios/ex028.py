import random
n_aleatorio = random.randint(1, 5)
n_escolhido = int(input('Escolha um número de 1 a 5: '))
if n_escolhido == n_aleatorio:
    print('Você acertou o número, venceu o game!')
else:
    print('Você não acertou, tente de novo!')
    print('O número aletório era {}!'.format(n_aleatorio))
