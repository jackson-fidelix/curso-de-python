#Faça um programa que tenha uma lista chamada números e duas funções chamadas
#sorteio() e somaPar(). A primeira função vai sortear 5 números e vai 
#colocá-los dentro da lista e a segunda função vai mostrar a soma 
#entre todos os valores PARES sorteados pela função anterior.
from random import randint


def sorteio(num):
    print('-=-='*15)
    print('Sorteando 5 valores da lista: ', end=" ")
    for i in range(num):
        sort = randint(0, 10)
        print(f' \033[1;43m {sort} \033[m', end=" ")
        numeros.append(sort)
    print('PRONTO!')

def somaPar(txt):
    soma_pares = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            soma_pares += v
    print(f'Somando os valores pares de \033[4;31m{numeros}\033[m, temos \033[1;42m {soma_pares} \033[m!')

    
numeros = []
sorteio(5)
somaPar(numeros)
