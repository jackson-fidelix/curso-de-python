# Faça um programa que leia 5 valores e guarde-os em uma lista. 
# Mostre qual foi o maior e o menor valor digitado e as suas respectivas posições.

valores = []
for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

maior_valor = max(valores)
menor_valor = min(valores)

posicoes_maior = []
for i in range(len(valores)):
    if valores[i] == maior_valor:
        posicoes_maior.append(i)

posicoes_menor = []
for i in range(len(valores)):
    if valores[i] == menor_valor:
        posicoes_menor.append(i)

print('===-'*12)
print(f'Essa é a lista completa: {valores}')
print(f'O maior valor é {max(valores)} e está nas posições {' ... '.join(map(str, posicoes_maior))}')
print(f'O menor valor é {min(valores)} e está nas posições {' ... '.join(map(str, posicoes_menor))}')
