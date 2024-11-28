# Crie um programa que vai ler vários númweos e colocar em uma lista.
# Depois disso, crie duas listas extras que vão contar apenas os valores pares
# e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
# listas geradas.
from time import sleep

numeros_geral = []
num_impar = []
num_par = []

while True:
    num_digitado = int(input('Digite um número: '))
    numeros_geral.append(num_digitado)
    escolha = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if escolha == 'S':
        continue
    elif escolha == 'N':
        break
    else: 
        print('Opção incorreta, tente novamente!')
        escolha = str(input('Deseja continuar? [S/N] ')).upper()[0]

print('===___==='*4)
print(f'A lista completa é: {numeros_geral}')
print('...'*15)
sleep(1)
print('\033[4;34mEstou fazendo algumas validações...\033[m')
sleep(2)
for i in range(len(numeros_geral)):
    if numeros_geral[i] % 2 == 0:
        num_par.append(numeros_geral[i])
    else:
        num_impar.append(numeros_geral[i])
print('\033[1;31mProntinho!!!\033[m')
sleep(2)
print(f'A lista de PARES é: \033[1;32m{num_par}\033[m')
print(f'A lista de ÍMPARES é: \033[1;33m{num_impar}\033[m')
