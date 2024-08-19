name = input('Digite nome completo de sua cidade: ')
editedname = name.split()
print('O nome inteiro de sua cidade é {}'.format(name))
print('Seu primeiro nome é: {}'.format(editedname[0]) if editedname[0].upper() == 'SÃO' else 'Seu primerio nome não começa com a palavra São!')