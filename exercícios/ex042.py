reta01 = int(input('Digite o comprimento de uma reta em centímetros: '))
reta02 = int(input('Digite o comprimento da segunda reta em centímetros: '))
reta03 = int(input('Digite o comprimento da terceira reta em centímetros: '))
if reta01 + reta02 > reta03 and reta02 + reta03 > reta01 and reta03 + reta01 > reta02:
    print('Excelente, nós temos um triângulo!')
    if reta01 == reta02 == reta03:
        print('Triângulo Equilátero!')
    elif reta01 == reta02 or reta02 == reta03 or reta03 == reta01:
        print('Triângulo Isósceles! ')
    else:
        print('Triângulo Escaleno!')
else:
    print('Essas retas NÃO FORMAM um triângulo!')