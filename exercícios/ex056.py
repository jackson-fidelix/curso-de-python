#leia nome, idade e sexo de 4 pessoas e mostre...
soma_idades = 0
idade_homem_velho = 0
nome_homem_velho = ''
mulheres_abaixo_de_vinte = 0
for i in range(1, 4+1):
    print(f'----- {i}ª pessoa -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M | F]: ')).upper()
    soma_idades += idade
    media_idades = int(soma_idades / 4)
    if sexo == 'M' and idade > idade_homem_velho:
        nome_homem_velho = nome
        idade_homem_velho = idade
    elif sexo == 'F' and idade < 20:
        mulheres_abaixo_de_vinte += 1

print('\033[1;33m=-\033[m'*30)
print(f'\033[1m A média de idade do grupo é {media_idades} anos.\033[m')
print(f'\033[1;32m O homem mais velho é o Sr. {nome_homem_velho} e ele possui {idade_homem_velho} anos!\033[m')
print(f'\033[1;35m Há {mulheres_abaixo_de_vinte} mulheres com menos de 20 anos! \033[m')
print('\033[1;33m=-\033[m'*30)
