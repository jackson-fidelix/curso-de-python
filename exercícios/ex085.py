#Crie um programa onde o usuário possa digitar sete valores numéricos e 
#cadastre-os em uma lista única que mantenha separado os valores pares
#e ímpares. No final mostre os valores pares e ímpares em ordem crescente

numeros = []
pares = []
impares = []

for i in range(0,7):
    num = int(input(f'Digite o {i + 1}º número: '))
    if num % 2 == 0: 
        pares.append(num)
    else:
        impares.append(num)    

numeros.append(pares)
numeros.append(impares)

print('-='*30)
print(f'A lista em ordem crescente de números pares é {sorted(numeros[0])}')
print(f'A lista em ordem crescente de números ímpares é {sorted(numeros[1])}')
