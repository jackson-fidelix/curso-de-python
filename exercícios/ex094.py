#Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando
#os dados de cada pessoa em um dicionário e todos os dicionários em um lista.
#No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com nome de todas as pessoas com idade acima da média

dict_pessoas = {}
list_pessoas = []
total_pessoas = 0
total_idades = 0
media_idade = 0
mulheres = []

while True:
    dict_pessoas['Nome'] = str(input('Nome: '))
    dict_pessoas['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    if dict_pessoas['Sexo'] != 'M' and dict_pessoas['Sexo'] != 'F':
        print('Opção de sexo inválida, tente novamente...')
        dict_pessoas['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    dict_pessoas['Idade'] = int(input('Idade: '))
    total_idades += dict_pessoas['Idade']
    if dict_pessoas['Sexo'] == "F":
        mulheres.append(dict_pessoas['Nome'])
    list_pessoas.append(dict_pessoas.copy())
    total_pessoas += 1
    media_idade = total_idades / total_pessoas
    
    resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if resp in 'N':
        print('---'*5)
        print('FINALIZANDO...')
        print('---'*5)
        break
    elif resp in 'S':
        continue
    else:
        print('Resposta incorreta, responda novamente!')
        resp = str(input('Deseja continuar [S/N]: ')).upper()[0]
print('=-=-'*15)
print(f'- O grupo tem {total_pessoas} pessoas.')
print(f'- A média de idade é de {media_idade:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end="")
for index, value in enumerate(mulheres):
    print(f'{value}', end=" | ")
print()
print(f'- A lista das pessoas que estão acima da Média: ')
for pessoa in list_pessoas:
    if pessoa['Idade'] > media_idade:
        print(f'Nome = {pessoa["Nome"]}; Sexo = {pessoa["Sexo"]}; Idade = {pessoa["Idade"]};')



