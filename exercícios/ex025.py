name = input('Digite seu nome completo: ')
splitname = name.split()
print('Seu nome é: {}'.format(name), 'e por óbvio contém a palavra Silva!' if 'SILVA' in name.upper() else '! \n Você não possui o nome Silva!')
