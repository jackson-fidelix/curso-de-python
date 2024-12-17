#Faça um programa que ajude um jogador da MEGA SENA
#a criar palpites. O programa vai perguntar quantos jogos serão gerados
#e vai sortear 6 números entre 1 e 60 para cada jogo, cadsastrando tudo
#em uma lista composta.
from random import randint
from time import sleep
print('---'*11)
print('JOGO NA MEGA SENA'.center(33))
print('---'*11)

resp = int(input('Quantos jogos você quer que eu sorteie? '))
print()
cont = 0
total_jogos = []
print(f"{f' SORTEANDO {resp} JOGOS ':=^33}")
while cont != resp:
    jogos = [randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60)]
    total_jogos.append(jogos[:])
    jogos.clear()
    cont += 1
print(f'{' < BOA SORTE! > ':=^33}')
for i, v in enumerate(total_jogos):
    print(f'Jogo {i+1}: {v}')
    sleep(1)
