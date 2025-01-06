#Faça um programa que tenha uma função chamada maior(), que recebe vários
#parâmetros com valores inteiros. Seu programa tem que analisar todos os 
#valores e dizer qual deles é o maior.
from random import randint
from time import sleep


def maior(rand):
    num_maior = 0
    print('-=-='*15)
    print('Atuallizando os valores...', flush=True)
    for i in range(rand):
        values = randint(1, 10)
        sleep(0.5)
        print(f'{values}',flush=True, end=" ")
        if num_maior == 0:
            num_maior = values
        elif values > num_maior:
            num_maior = values
    print(f'Foram informados {rand} valores ao todo.')
    print(f'O maior valor informado foi {num_maior}.')


maior(randint(0, 10))
maior(randint(0, 10))
maior(randint(0, 10))
maior(randint(0, 10))
maior(randint(0, 10))