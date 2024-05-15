salario = float(input('Digite seu salário atual: '))
taxa_aumento = float(salario * 0.15)
novo_salario = float(salario + taxa_aumento)
print('Conforme mencionado, seu SALÁRIO ATUAL é de R${:.2f}. \n'
      'Seu novo SALÁRIO, considerando a taxa de 15% de aumento é de R${:.2f}!'.format(salario, novo_salario))