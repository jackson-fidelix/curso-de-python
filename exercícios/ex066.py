# Leia vários números inteiros e quando digitado 999 pare usando BREAK!
# O sistema precisa dizer quantos números foram digitados e qual o valor da soma deles
num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('Digite um número \033[1;32minteiro\033[m, (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Ao todo foram digitados \033[1;34m{cont}\033[m números!')
print(f'A soma destes é \033[1;31m{soma}\033[m!!')