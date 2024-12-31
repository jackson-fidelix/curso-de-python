#Aprimore o desafio 93 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento
#de cada jogador.
jogadores = []
estatisticas = {}


while True:
    nome = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    gols = []
    totgols = 0
    for i in range(1, partidas + 1):
        gol = int(input(f'  Quantos gols o jogador fez na {i}º partida? '))
        gols.append(gol)
        totgols += gol
    estatisticas['Nome'] = nome
    estatisticas['Gols'] = gols
    estatisticas['Total'] = totgols
    jogadores.append(estatisticas.copy())
    estatisticas.clear()

    resp = str(input("Deseja continuar? [S/N]")).upper()[0]
    if resp in "S":
        continue
    elif resp in "N":
        break
    else:
        print("Opção incorreta, tente novamente!")
        resp = str(input("Deseja continuar? [S/N]")).upper()[0]    

print('=-=-'*13)
print(f'{"Cód.":<4} {"Nome":<15} {"Gols":<15} {"Total":^8}')
print('----'*12)
for idx, val in enumerate(jogadores):
    print(f"{idx:^4} {val['Nome']:<15} {str(val['Gols']):<15} {val['Total']:^8}")
print('=-=-'*13)

while True:
    opc = int(input('Deseja visualizar qual jogador? [999 interrompe]: '))
    print('=-=-'*13)
    if opc == 999:
        print(f'{" FINALIZANDO... ":*^30}')
        print(f'{" VOLTE SEMPRE ":=^30}')
        break
    elif 0 <= opc < len(jogadores):
        print('----'*12)
        print(f'--LEVANTAMENTO DO JOGADOR {jogadores[opc]['Nome']}:')
        for idx, val in enumerate(jogadores[opc]['Gols']):
            print(f'No jogo {idx + 1}, fez {val} gol(s).'.center(30))
        print('----'*12)
    else:
        print('Aluno não encontrado!!!')
        opc = int(input('Deseja visualizar qual jogador? [999 interrompe]: '))
