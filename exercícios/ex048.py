#soma entre números ímpares de 1 a 500 e multiplos de 3.
soma_impar = 0
for c in range(1, 500, 1):
    if c % 2 != 0 and c % 3 == 0:
        print(c)
        soma_impar += c
print('A soma de todos os números ímpares e múltiplos de três, de 1 a 500 é {}'.format(soma_impar))