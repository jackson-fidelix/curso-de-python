#jogue par ou ímpar com o computador. O jogo só sera interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
vitoria = 0
print('=-'*20)
print('\033[1;32mVamos jogar PAR ou ÍMPAR!\033[m'.center(50))
print('=-'*20)
while True:
    num_jogador = int(input('Diga um valor: '))
    decisao = str(input('PAR ou ÍMPAR? [P/I] ')).upper().strip()
    if decisao != 'P' and decisao != 'I':
        print('\033[4;31mOpção invláida. Tente novamente!\033[m')
        continue
    pc = randint(1,20)
    somatoria = num_jogador + pc
    print(f'Você escolheu {num_jogador} e o PC {pc}. Total deu {somatoria} -', end=" ")
    if somatoria % 2 == 0:
        print('\033[1;33mDeu PAR!\033[m')
        print('--'*20)
        resultado = 'P'
        if decisao == resultado:
            vitoria += 1
            print('\033[4;32mVocê venceu, vamos jogar novamente!\033[m')
            continue
        else:
            print('\033[4;31mVocê perdeu!')
            break
    else: 
        print('\033[1;34mDeu ÍMPAR!\033[m')
        print('--'*20)
        resultado = 'I'
        if decisao == resultado:
            vitoria += 1
            print('\033[4;32mVocê venceu, vamos jogar novamente!\033[m')
            continue
        else:
            print('\033[4;31mVocê perdeu!')
            break
print('\033[7;33m!GAME OVER!\033[m')
print(f'\033[4;34mVocê venceu {vitoria} vezes!\033[m')
