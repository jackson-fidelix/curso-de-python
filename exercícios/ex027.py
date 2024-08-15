nome_completo = input('Digite seu nome completo: ')
print('De acordo com o que foi digitado, seu nome completo é: {}!'.format(nome_completo))
nome_split = nome_completo.split()
print('Seu primeiro nome é {} e o sobrenome {}!'.format(nome_split[0], nome_split[-1]))