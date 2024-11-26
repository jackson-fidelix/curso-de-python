# Faça um programa que leia 5 valores e guarde-os em uma lista. 
# Mostre qual foi o maior e o menor valor digitado e as suas respectivas posições.

valores = []
for i in range(0, 5):
    valores.append(int(input('Digite um valor:')))
print('===-'*12)
print(f'Essa é a lista completa: {valores}')
print(f'O maior valor é {max(valores)} e está na {valores.index(max(valores))+1}° posição.')
print(f'O menor valor é {min(valores)} e está na {valores.index(min(valores))+1}° posição.')