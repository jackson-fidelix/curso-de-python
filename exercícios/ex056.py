#leia nome, idade e sexo de 4 pessoas e mostre
soma_idades = 0
idade_homem_velho = 0
nome_homem_velho = ''
mulheres_abaixo_de_vinte = 0
for i in range(1, 4+1):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual é seu sexo?(M = Masculino e F = Feminino): ')).upper()
    soma_idades += idade
    media_idades = int(soma_idades / 4)
    if sexo == 'M' and idade > idade_homem_velho:
        nome_homem_velho = nome
        idade_homem_velho = idade
    elif sexo == 'F' and idade < 20:
        mulheres_abaixo_de_vinte += 1
    elif sexo != 'M' or sexo != 'F':
        print('Opção de sexo inválida!')
        
print('=-'*20)
print(f'A média de idade do grupo é {media_idades} anos.')
print(f'O homem mais velhor é o Sr. {nome_homem_velho} e ele possui {idade_homem_velho} anos!')
print(f'Há {mulheres_abaixo_de_vinte} mulheres com menos de 20 anos!')
print('=-'*20)