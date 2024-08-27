salario = int(input('Digite o seu salário: '))
if salario <= 1250.00:
    aumento10 = salario*0.10
    salario_novo = salario+aumento10
    print('Esse é o novo salário, considerando o aumento de 10% que prometemos!')
    print('O valor de aumento é de {:.2f}!'.format(aumento10))
    print('Salário Novo: {:.2f}'.format(salario_novo))
else:
    aumento15 = salario*0.15
    salario_novo = salario+aumento15
    print('Esse é o novo salário, considerando o aumento de 15% que prometemos!')
    print('O valor de aumento é de {:.2f}!'.format(aumento15))
    print('Salário Novo: {:.2f}'.format(salario_novo))