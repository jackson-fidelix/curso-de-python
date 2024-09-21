#digite um numero e descubra se ele é primo
num = int(input('Digite um número: '))
div = 0
divisores = []
for i in range(1, num+1):
    if num % i == 0:
        div += 1
        divisores.append(i) 
if div == 2:
    print('Esse número é primo, pois tem apenas \033[1;32m{}\033[m divisores!'.format(div))
    print('Os divisores de \033[1;32m{}\033[m são: \033[1;32m{}\033[m'.format(num, divisores))
else:
    print('Esse número não é primo, pois é divisível por \033[1;31m{}\033[m divisores!'.format(div))
    print('Os divisores de \033[1;31m{}\033[m são: \033[1;31m{}\033[m'.format(num, divisores))