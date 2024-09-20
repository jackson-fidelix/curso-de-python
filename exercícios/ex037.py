num_inteiro = int(input('Digite um número inteiro qualquer: '))
print('===-===-===-===-===-===-===-===-===')

print('Digite 1 para conversão Binária:')
print('Digite 2 para conversão Octal: ')
print('Digite 3 para conversão Hexadecimal: ')
num_escolhido = int(input('>>> '))

if num_escolhido == 1:
    print('\033[1;32mVocê escolhou a opção 1 e sua base Binária é {}! \033[m'.format(bin(num_inteiro)[2:]))
elif num_escolhido == 2:
    print('\033[1;33mVocê escolheu a opção 2 e sua base Octal é {}! \033[m'.format(oct(num_inteiro)[2:]))
elif num_escolhido == 3:
    print('\033[1;36mVocê escolheu a opção 3 e a sua base Hexadecimal é {}!\033[m'.format(hex(num_inteiro)[2:]))
else:
    print('\033[4;31;43mVocê não selecionou uma opção existente!\033[m')