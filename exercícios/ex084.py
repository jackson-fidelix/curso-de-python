#faça um programa que lea oo nome e peso de várias pessoas, guardando tudo
#em uma lista . No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas
#C) Uma listagem com as pessoas mais leves

pessoas = list()
dado = list()
peso_maior = peso_menor = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    
    for p in pessoas:
        if peso_maior == 0 and peso_menor == 0:
            peso_maior = peso_menor = p[1]
        elif p[1] < peso_menor:
            peso_menor = p[1]
        elif p[1] > peso_maior:
            peso_maior = p[1]

    resp = (str(input('Quer continuar? [S/N] '))).upper()[0]
    if resp == 'S':
        continue
    elif resp == 'N':
        break
    else:
        print('Resposta incorreta... Tente novamente!')
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
print('=-='*10)
print(f'Os dados foram {pessoas}')
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso é {peso_maior}Kg. Peso de ', end="")
for p in pessoas:
    if p[1] == peso_maior:
        print(f'{p[0]}', end='| ')
    
print(f'\nO menor peso é {peso_menor}Kg. Peso de ', end="")
for p in pessoas:
    if p[1] == peso_menor:
        print(f'{p[0]}', end='| ')
print()        
print('=-='*10)
