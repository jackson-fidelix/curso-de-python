#escolha 6 número e faça a soma somente dos pares
soma_pares = 0
for i in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma_pares += num
print('A soma dos números pares digitados é {}!'.format(soma_pares))