#Faça um programa que tenha uma função chamada ficha(), que receba dois 
#parâmetros opcionais: o NOME de um jogador e quantos GOLS ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo 
#que algum dado não tenha sido informado corretamente

def ficha(name = "", goal = 0):
    if not name:
               name = "<desonhecido>"
    if not goal:
            goal = 0
    print(f'O jogador {name.upper()} fez {goal} gol(s) no campeonato.')


 #programa principal
nome = input('Nome do Jogador: ').strip()
gol = input('Número de Gols: ').strip()
ficha(nome, gol)