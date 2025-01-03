#Faça um programa qye tenha uma função chamada área(),
#que receba as dimensões de um terreno retangular (largura e 
#comprimento) e mostre a área do terreno.

def área(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {area:.2f}m².')


largura = float(input('LARGURA (m): '))
comprimento = float(input('ALTURA (m): '))
área(largura, comprimento)
