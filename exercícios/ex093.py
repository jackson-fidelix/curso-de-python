#Crie um programa que gerencie o aproveitamento de um jogador
#de futebol, O programa vair ler o nome do jogador, quantas partidas 
#ele jogou. Depois, lerá a quantidade de gols feitos em casa partida. 
#No final, tudo isso será guardado em um dicionário, incluindo o total de
#gols feitos durante o campeonato.

estatisticas = {}
nome = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {nome} jogou? '))

gols = []
totgols = 0
for i in range(1, partidas +1):
    gol = int(input(f'Quantos gols o jogador fez na {i}º partida? '))
    gols.append(gol)
    totgols += gol
#colocando tudo em um dicionário para a 1º solução
estatisticas['Nome'] = nome
estatisticas['Gols'] = gols
estatisticas['Total'] = totgols
print('=-=-'*15)
print(estatisticas)
print('=-=-'*15)
#na segunda solução, precisamos de um for para representar os dados FORMATADOS
for key, value in estatisticas.items():
    print(f'O campo {key} tem o valor {value}.')
print('=-=-'*15)
print(f'O jogador {estatisticas["Nome"]} jogou {partidas} partidas!')
for idx, value in enumerate(gols):
    print(f'   => Na partida {idx + 1}, fez {value} gol(s).')
print(f'Foi um total de {estatisticas["Total"]} gols.')
