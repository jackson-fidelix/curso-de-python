#Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastreo-os em uma lista. Já na posição correta
#de inserção(sem usar o sort(). No final, mostre a lista ordenada
numeros = []

for i in range(5):
    num = int(input('Digite um valor numérico: '))

    if len(numeros) == 0:
        numeros.append(num)
        print('Número adicionado com sucesso!')
    elif num > numeros[-1]:
        numeros.append(num)
        print(f'Número adicionado no final da lista!')
    else:
        for valor in range(len(numeros)):
            if num <= numeros[valor]:
                numeros.insert(valor, num)
                print(f'Número {num} adicionado na posição {valor} da lista!')
                break            
print(f'A lista Ordenada é: {numeros}')
