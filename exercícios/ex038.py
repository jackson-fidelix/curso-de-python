n1 = int(input('Digite um número inteiro qualquer: '))
n2 = int(input('Digite outro número inteiro qualquer: '))

if n1 > n2:
    print('O primeiro número é {} e ele é maior que o segundo!'.format(n1))
elif n2 > n1:
    print('O segundo número é {} e ele é maior que o primeiro!'.format(n2))
else:
    print('Não existe valor maior, ambos são iguais!')