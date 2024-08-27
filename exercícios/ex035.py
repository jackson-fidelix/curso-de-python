reta1 = int(input('Digite o valor da primeira reta em METROS: '))
reta2 = int(input('Digite o valor da segunda reta em METROS: '))
reta3 = int(input('Digite o valor da terceira reta em METROS: '))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('Parabéns!!! \n Essas retas formam um triângulo!')
else:
    print('Algo está errado, essas retas não formal um triângulo!')