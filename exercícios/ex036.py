valor_casa = float(input('Qual é o valor da casa que você deseja comprar? \n'))
salario = float(input('Qual é o seu salário? \n'))
anos = int(input('Quantos anos de financiamento? '))
prestação = valor_casa / (anos * 12)
mínimo = salario * 0.3

print('Considerando o valor da casa de R$\033[1;33m{:.2f}\033[m em \033[1;32m{}\033[m anos'.format(valor_casa, anos), end='')
print(' a prestação será de R$ {:.2f}!'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo negado! Prestação maior que 30% do seu salário!')
      