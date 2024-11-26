# num = [2, 5, 9, 1]
# num[2] = 4
# num.append(9)
# num.sort(reverse=True)
# print(num)
# num.insert(2, 0)
# print(num)
# num.pop()
# print(num)
# print(f'O tamanho da lista é {len(num)}')

valores = [5, 9, 4, 10]

for index, valor in enumerate(valores):
    print(f'Na posição {index} encontrei o valor {valor}! ')
print('Cheguei ao final da lista valores.')

lista = []
for i in range(0, 5):
    lista.append(int(input('Digite um número: ')))

for index, list in enumerate(lista):
    print(f'Na posição {index} encontrei o valor {list}! ')
print('Chwguei ao final da lista.')