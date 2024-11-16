# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# Quantas vezes apareceu o valor 9
# Em que posição foi digitado o primeiro valor 3
# Quais foram os números pares
num_list = []
quant_nove = 0
num_pares = []

for i in range (1, 5):
    num = int(input('Digite um número: '))
    num_list.append(num)
    if num == 9:
        quant_nove += 1
    elif num % 2 == 0:
        num_pares.append(num)


num_tuple = tuple(num_list) 
print(f'A Tupla criada foi {num_tuple}')
print(f'O número nove aparece {quant_nove} vez(es)!')
if 3 in num_tuple:
    print(f'O valor 3 aparece na posição {num_tuple.index(3) + 1}')
else:
    print('Essa TUPLA não contém o número 3!')
print(f'Os número(s) pares são {num_pares}!')

