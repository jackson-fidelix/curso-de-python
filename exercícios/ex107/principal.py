#Crie um módulo chamado moeda.py quye tenha as funções incorporadas aumentar(), 
#diminuir(), dobro() e metade(). Faça também um programa que importe esse 
#módulo e use algumas dessas funções.
import sys
sys.path.append('e:\MeusProjetos\curso-de-python\exercícios')
from ex107 import moedas

price = float(input('Digite o preço: R$'))
print(f'A metade de {price} é {moedas.metade(price)}')
print(f'O dobro de {price} é {moedas.dobro(price)}')
print(f'Aumentando 10%, temos {moedas.aumentar(price, 10)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(price, 13)}')

