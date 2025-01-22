#Faça um programa que tenha uma função chamada ficha(), que receba dois 
#parâmetros opcionais: o NOME de um jogador e quantos GOLS ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo 
#que algum dado não tenha sido informado corretamente

def ficha(name = "<desonhecido>", goal = 0):
    print(f'O jogador {name.upper()} fez {goal} gol(s) no campeonato.')


 #programa principal
nome = str(input('Nome do Jogador: ')).strip()
gol = str(input('Número de Gols: ')).strip()
if gol.isnumeric():
        gol = int(gol)
else:
        gol = 0
if nome == '':
        ficha(goal=gol)
else:
        ficha(nome,gol)