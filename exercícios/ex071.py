#crie um caixa eletrônico, no início deverá perguntar ao usuário qual o valor a ser sacado e o programa informará quantas cédulas de cada valor serão entregues.
# considere que o caixa possui cédulas de R$50,R$20,R$10 e R$1

print('==='*10)
print('BANCO J & A'.center(30))
print('==='*10)

saque = int(input('Qual é o valor que deseja sacar? '))

while True:
    if saque != 0:
        # primeiro dividimos pelo MAIOR valor de cédula, para vermos quantas cedulas de 50 o usuário receberá
        cedulas_50 = int(saque / 50)
        resto_50 = int(saque % 50)
        print(f'Total de {cedulas_50} cédulas de R$50,00')
        if resto_50 != 0:
            #feito isso, agora fazemos o mesmo processo com o SEGUNDO maior valor, utilizando o resto da PRIMEIRA divisão
            cedulas_20 = int(resto_50 / 20)
            resto_20 = int(resto_50 % 20)
            print(f'Total de {cedulas_20} cédulas de R$20,00')
            if resto_20 != 0:
                #feito isso, agora fazemos o mesmo processo com o TERCEIRO maior valor, utilizando o resto da SEGUNDA divisão
                cedulas_10 = int(resto_20 / 10)
                resto_10 = int(resto_20 % 10)
                print(f'Total de {cedulas_10} cédulas de R$10,00')
                if resto_10 != 0:
                    #feito isso, agora fazemos o mesmo processo com o QUARTO maior valor, utilizando o resto da TERCEIRA divisão
                    cedulas_1 = int(resto_10 / 1)
                    print(f'Total de {cedulas_1} cédulas de R$1,00')        
    break




