#crie um programa que tenha um TUPLA totalmente preenchida de 0 a 20(por extenso). Seu programa deverá ler o número que o usuário digitar nesse intervalo e imrpimí-lo por extenso.

numbers = ('ZERO','UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'CATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

while True:
    escolha = int(input('Digite um número entre 0 e 20: '))

    if escolha >= 0 and escolha <= 20:
        break
    else:
       print('Número incorreto...Tente novamente... ')

print(f'Você digitou o número {numbers[escolha]}!')

