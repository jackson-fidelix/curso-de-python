#Crie um programa onde 4 jogadores joguem dado e tenham
#resultados aleatórios. Guarde esses resultados em um 
# dicionário.No final, coloque esse dicionário em ordem, 
# sabendo que o vencedor tirou o maior número no dado.
from random import randint

totjogadores = []
for i in range(1,5):
    jogador = {}
    num_dado = randint(1, 6)
    print(f'O jogador {i} tirou {num_dado}')
    jogador['num_jogador'] = i
    jogador['num_dado'] = num_dado
    totjogadores.append(jogador.copy())
print('-=-'*8)

lista_ordenada = sorted(totjogadores,reverse=True, key=lambda item:item['num_dado'])

for index, value in enumerate(lista_ordenada):
    print(f'{index + 1}ºLugar - player {value['num_jogador']} com {value['num_dado']}')
    print('---'*8)
