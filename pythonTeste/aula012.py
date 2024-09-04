nome = str(input('Qual é o seu nome?\n'))
if nome == 'Jackson':
    print('WHAT NAME AMAZING!!!')
elif nome == 'João' or nome == 'Maria' or nome == 'Mateus':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Creuza Josefina Ronalda':
    print('Seu nome é estranho!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))