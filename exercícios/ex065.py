
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
    continuar = str(input('Deseja continuar [S/N]? ')).upper() 
    if continuar == 'S':
        if maior == 0 and menor == 0:
            maior = numero
            menor = numero
        elif numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    elif continuar == 'N':
        continuar = 'NÃO'
        if maior == 0 and menor == 0:
            maior = numero
            menor = numero
        elif numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
        print('| FIM DO PROGRAMA |')

media = soma / contador
print('==='*16)
print(f'Ao todo foram digitados {contador} números, e a média é {media}!')
print(f'O MAIOR número é {maior} e o MENOR é {menor}!')
print('==='*16)