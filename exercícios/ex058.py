from random import randint
num_aleatorio = randint(0,10)
num_escolhido = 99
palpites = 0
num_escolhido = int(input('Escolha um número de 0 a 10: '))
palpites += 1

while num_escolhido != num_aleatorio:
    if num_escolhido > num_aleatorio:
        print('Menos... tente de novo!')
        num_escolhido = int(input('Qual é o seu palpite? '))
        palpites += 1
    elif num_escolhido < num_aleatorio:
        print('Mais... tente de novo!')
        num_escolhido = int(input('Qual é o seu palpite? '))
        palpites += 1
print('Parabéns, você acertou!')
print(f'Você teve {palpites} palpite(s)!')
