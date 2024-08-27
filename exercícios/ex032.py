ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0:
    print('O ano digitado foi {} e ele é um ano bissexto!'.format(ano))
else:
    print('O ano {} NÃO é um ano biossexto!'.format(ano))