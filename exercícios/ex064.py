#some alguns valores e quando o usuário digitar 999 pare o programa e imprima a soma e a quantidade de números que foram digitados 
soma = 0
contador = 0
numero = 0

while numero != 999:
    numero = int(input('Digite um valor qualquer de 0 a 999: '))
    if numero > 999 or numero < 0:
        print('Você digitou um número inválido!!!')
        continue
    elif numero == 999:
        break
    soma += numero
    contador += 1

print('==='*13)
print('| FIM DO PROGRAMA |')
print(f'Ao todo foram digitados \033[1;31m{contador}\033[m números válidos! ')
print(f'A soma deles é \033[1;32m{soma}\033[m!')
print('==='*13)