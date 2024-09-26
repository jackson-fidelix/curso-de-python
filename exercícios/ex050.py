#escolha 6 número e faça a soma somente dos pares
soma_pares = 0
cont = 0
for i in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma_pares += num
        cont += 1
print('Há {} números pares e a soma foi {}!'.format(cont, soma_pares))