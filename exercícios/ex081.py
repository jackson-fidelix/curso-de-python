#Crie um programa que vai ler vários números e colocar em uma lista
#Mostre, quantos números foram digitados, lista de valores de forma decrescente
# e por último, se o valor 5 está na lista.
number_list = []
cont_number = 0
while True:
    number = int(input('Digite um valor: '))
    number_list.append(number)
    cont_number += 1
    escolha = str(input('Quer continuar? [S/N] ')).upper()[0]
    if escolha == 'S':
        continue
    elif escolha == 'N':
        break
    else:
        escolha = str(input('Opção errada! Deseja prosseguir? [S/N]')).upper()[0]

print(number_list)
print(f'Ao todo foram digitados {cont_number} números!')
print(f'A lista Decrescente é {sorted(number_list,reverse=True)}')
if 5 in number_list:
    print(f'O número 5 está na lista na posição {number_list.index(5)}')
else:
    print('O número 5 não está na lista!')
