#faça um programa que mostre a tabuada de acordo com o número digitado pelo usuário e pare quando for digitado algum número menor que 0
num = 1
while num >= 0:
    num = int(input('\033[1;32m Digite um número para saber sua tabuada: \033[m'))
    if num < 0:
        break
    elif num == 0:
        print('\033[1;31mQualquer número x 0 é ZERO!\033[m')
        continue
    print('='*20)
    print(f'Segue a tabuada do {num}!')
    for i in range(1,11,1):
        tabuada = num * i
        print(f'{num} x {i} = {tabuada}')
    print('='*20)    