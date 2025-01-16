def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
#com return podemos personalizar a resposta

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')