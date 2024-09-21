#refazer a tabuada do ex09 com estrutura de repetição
num_tabuada = int(input('Digite a tabuada que você deseja gerar: '))
for i in range(1, 10+1):
    multiplicacao = num_tabuada * i
    print('{} x {} = {}'.format(num_tabuada, i, multiplicacao))