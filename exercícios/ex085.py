#Crie um programa onde o usuário possa digitar sete valores numéricos e 
#cadastre-os em uma lista única que mantenha separado os valores pares
#e ímpares. No final mostre os valores pares e ímpares em ordem crescente

numeros = [[], []]

for i in range(0,7):
    valor = int(input(f'Digite o {i + 1}º número: '))
    if valor % 2 == 0: 
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)    

print('-=-='*15)
print(f'A lista em ordem crescente de números pares é {sorted(numeros[0])}')
print(f'A lista em ordem crescente de números ímpares é {sorted(numeros[1])}')
print('-=-='*15)
