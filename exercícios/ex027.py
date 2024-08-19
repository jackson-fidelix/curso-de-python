nome_completo = str(input('Digite seu nome completo: ')).strip()
print('De acordo com o que foi digitado, seu nome completo é: {}!'.format(nome_completo))
novo_nome = nome_completo.split()
print('Seu primeiro nome é {} e o sobrenome {}!'.format(novo_nome[0], novo_nome[-1]))