#leia 7 anos de nascimento e mostre quantas pessoas tem maioridade e minoridade
from datetime import date
maioridade = 0
minoridade = 0
for i in range(1, 7+1):
    ano = int(input(f'Digite ano de nascimento da {i}ª pessoa: '))
    idade = date.today().year - ano
    if idade >= 21:
        maioridade += 1
    else:
        minoridade += 1
print(f'A quantidade de pessoas que atingiram sua MAIORIDADE é \033[1;32m{maioridade}\033[m e há \033[1;31m{minoridade}\033[m pessoa(s) ainda com MINORIDADE!')