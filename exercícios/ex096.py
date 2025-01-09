#Faça um programa qye tenha uma função chamada área(),
#que receba as dimensões de um terreno retangular (largura e 
#comprimento) e mostre a área do terreno.

def área(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {area:.2f}m².')


print('=-'*10)
print('Controle de Terrenos')
print('=-'*10)
larg = float(input('LARGURA (m): '))
comp = float(input('ALTURA (m): '))
área(larg, comp)
