#leia varios números inteiros e no final da execução mostre a media deles e qual foi o maior e o menor valor
#o campo soma foi uma incrementada
soma = 0
contador = 0
numero = 0
continuar = 'SIM'
maior = 0
menor = 0

while continuar != 'NÃO':
    numero = int(input('Digite um valor qualquer: '))
    soma += numero
    contador += 1
    if maior == 0 and menor == 0:
        maior = numero
        menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    continuar = str(input('Deseja continuar [S/N]? ')).upper() 
    if continuar == 'S':
        continue
    elif continuar == 'N':
        continuar = 'NÃO'
        print('| FIM DO PROGRAMA |')
        break
    else:
        print('Você digitou a opção errada!')
        continuar = str(input('Deseja continuar [S/N]? ')).upper() 

media = soma / contador
print('==='*16)
print(f'Ao todo foram digitados \033[7;44m {contador} \033[m números! e a MÉDIA é \033[1;33m{media}\033[m!')
print(f'A SOMA destes é \033[1;32m{soma}\033[m!')
print(f'O MAIOR número é \033[1;36m{maior}\033[m e o MENOR é \033[1;31m{menor}\033[m!')
print('==='*16)