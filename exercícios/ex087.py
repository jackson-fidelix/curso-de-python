#Aprimore o desafio anterior, mostrando no final: 
#A)A soma de todos os valores pares digitados. 
#B)A soma dos valores da terceira coluna
#C)O maior valor da segunda linha

soma_pares = 0
soma_TerColuna = 0

matriz = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {[l, c]}: '))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            soma_TerColuna += matriz[l][c]

print('=-'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end=" ")
    print()
print('=-'*22)
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_TerColuna}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
print('=-'*22)
