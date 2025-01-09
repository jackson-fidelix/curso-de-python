#Faça um programa que tenha uma função chamada contador(), que receba três
#parâmetros: início, fim e passo e realize a contagem. Seu programa tem que 
#realizar três contagens através da função criada:
#A)De 1 até 10, de 1 em 1
#B)De 10 até 0, de 2 em 2
#C) uma contagem personalizada.
from time import sleep

def contador(início,fim, passo):
    if passo == 0:
        passo = 1 
    if início > fim and passo < 0: 
        print(f'Contagem de {início} até {fim} de {-passo} em {-passo}')
        for c in range(início, fim - 1, passo):
            print(f'{c}', end=" ", flush=True)
            sleep(0.8)
        print('FIM!')
        print('-=-='*11)
    elif início > fim and passo > 0:
        print('-=-='*11)
        print(f'Contagem de {início} até {fim} de {passo} em {passo}')
        for c in range(início, fim - 1, -passo):
            print(f'{c}', end=" ", flush=True)
            sleep(0.8)
        print('FIM!')
    else:  
        print(f'Contagem de {início} até {fim} de {passo} em {passo}')
        for c in range(início, fim + 1, passo):
            print(f'{c}', end=" ", flush=True)
            sleep(0.8)
        print('FIM!')
        print('-=-='*11)


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é a sua vez de personalizar a contagem!')
inicial   = int(input('INÍCIO: '))
final = int(input('FIM: '))
passo = int(input('PASSO: '))
print('-=-='*11)
contador(inicial, final, passo)
