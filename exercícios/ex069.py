#leia a idade e sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar.
#No final mostre: quantas pessoas tem + de 18 anos, quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos
older = 0
male = 0
young_women = 0
print('='*30)
print('\033[1;33mCADASTRO DE PESSOAS\033[m'.center(40))
print('='*30)

while True:
    sex = str(input('Digite seu sexo [F/M]: ')).upper().strip()
    if sex != 'F' and sex != 'M':
        print('\033[4;31mSexo incorreto, digite novamente!\033[m')
        continue
    elif sex == 'M':
        male += 1
    age = int(input('Qual é a sua idade? '))
    if age > 18:
        older += 1
    if sex == 'F' and age < 20:
            young_women += 1
    print('-'*30)
    decision = str(input('Deseja parar? [S/N] ')).upper().strip()
    print('-'*30)
    if decision == 'S':
        break
    elif decision == 'N':
        continue
    else:
        print('\033[4;31mOpção incorreta, tente novamente.\033[m')

print('\033[1;30;47m=\033[m'*40)
print(f'\033[1;33mHá {older} pessoas com mais de 18 anos!\033[m')
print(f'\033[1;34mHá {male} homens cadastrados!\033[m')
print(f'\033[1;32mHá {young_women} mulheres com menos de 20 anos!\033[m')
print('\033[1;30;47m=\033[m'*40)