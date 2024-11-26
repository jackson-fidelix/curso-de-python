#Crie um programa onde o usuário possa digitar vários valores 
#numéricos e cadastre-os em uma lista. Caso o número já existra lá dentro, 
#ele não será adicionado. No final, serão exibidos todo os valores únicos digitados, 
#em ordem crescente.

number_list = []

while True:
    num = int(input('Digite um número para adicionar: '))
    if num not in number_list:
        number_list.append(num)
        print('Número adicionado com sucesso!')
    else:
        print('Número duplicado... Tente novamente!')
    start = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if start in 'S':
        continue
    elif start in 'N':
        break
    else:
        print('Resposta incorreta... Tente novamente!')
        start = str(input('Deseja continuar? [S/N] ')).upper()[0]
print(f'Você digitou os valores {sorted(number_list)}')
