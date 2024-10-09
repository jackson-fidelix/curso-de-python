from random import randint
num_aleatorio = randint(0,10)
num_escolhido = 99
palpites = 0
while num_escolhido != num_aleatorio:
    print('Tente outra vez!')
    num_escolhido = int(input('Escolha um número de 0 a 10: '))
    palpites += 1
print('Parabéns, você acertou!')
print(f'Você teve {palpites} palpite(s)!')