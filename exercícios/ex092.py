#Crie um programa que leia nome, ano de nascimento e carteira de trabalho,
#cadastre-os (com a idade) em um dicionário, se por casado a CTPS for 
#diferente de ZERO, o dicionário receberá também o ano de contratação e o 
#salário. Calcule e acrescente, além da idade.com quantos anos a pessoa 
#vai se aposentar.

from datetime import datetime

dados = {}
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.today().year - nascimento
dados['Ctps'] = int(input('Carteira de Trabalho [0 não tem]: '))

if dados['Ctps'] == 0:
    print('\033[1;31m===\033[m'*14)
    for k,v in dados.items():
        print(f'{k} tem o valor {v}')
elif dados['Ctps'] != 0:
    dados['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário [R$]: '))
    dados['Aposentadoria'] = dados['Idade'] + (35 - (datetime.today().year - dados['Ano de Contratação']))
    print('\033[1;31m===\033[m'*14)
    for k,v in dados.items():
        print(f'\033[1;33m{k}\033[m tem o valor \033[1;32m{v}\033[m')
    print('\033[1;31m===\033[m'*14)
