import random

print('BEM-VINDO AO JOKENPÔ!')
print('===--===--===--===--===--===--===--===--===')
print('Escolha uma das alternativas: ')
print('1 - Pedra')
print('2 - Tesoura')
print('3 - Papel')
print('===--===--===--===--===--===--===--===--===')
jogador = int(input('Qual opção você escolheu(1, 2 ou 3)? '))
pc = random.randint(1,3)

opcoes = {1: 'PEDRA', 2: 'TESOURA', 3: 'PAPEL'}

if jogador == 1 and pc == 2 or jogador == 2 and pc == 3 or jogador == 3 and pc == 1:
    print('Você VENCEU, pois escolheu {0} e o PC escolheu {1}!'.format(opcoes[jogador], opcoes[pc]))
elif jogador == pc:
    print('EMPATE!!! Você escolheu {0} e o PC também! \n Jogue novamente!'.format(opcoes[jogador]))
else:
    print('Você PERDEU, pois escolher {0} e o PC escolheu {1}! Jogue de novo!'.format(opcoes[jogador], opcoes[pc]))