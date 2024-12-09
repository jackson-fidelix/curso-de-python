#Crie um programa que leia nome e duas notas de vários alunos e
#guarde tudo em uma lista composta. No final, mostre o boletim
#contendo a média de cada um e permita que o usuário possa mostrar
#as notas de cada aluno individualmente.

boletim = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])

    resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if resp == 'S':
        continue
    elif resp == 'N':
        break
    else:
        print('Resposta incorreta... Tente novamente!')
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
print('-='*15)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*15)
for i, aluno in enumerate(boletim):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.2f}')
    print()
print('--'*15)

while True:
    opc = int(input('Mostrar notas de qual aluno? [999 para interromper]: \n'))
    print('===='*10)
    if opc == 999:
        print('Finalizando...')
        print(f'{"VOLTE SEMPRE":=^30}')
        break
    elif opc >= 0 and opc < len(boletim):
        print(f'As notas de {boletim[opc][0]} são {boletim[opc][1]}')
        print('---'*10)
    else:
        print("Aluno não encontrado... Tente novamente!")
