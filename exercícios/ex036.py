valor_casa = float(input('Qual é o valor da casa que você deseja comprar? \n'))
salario = float(input('Qual é o seu salário? \n'))
parcela = salario * 0.3
quant_ano = (valor_casa / parcela) / 12
print('Considerando o valor da casa de R$\033[1;33m{:.2f}\033[m e o salário atual de R$\033[1;32m{:.2f}\033[m, \n'
      'sabendo que será consumido apenas 30% do salário, equivalente a R$\033[1;31m{:.2f}\033[m, \n'
      'a casa será paga em \033[36m{:.2f}\033[m anos!'.format(valor_casa, salario, parcela, quant_ano))