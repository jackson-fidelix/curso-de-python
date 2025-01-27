#Adapte o código do desafio 107, criando uma função adicional chamada  
#moeda() que consiga mostrar os valores coomo um valor monetário formatado 
import sys
sys.path.append('e:\MeusProjetos\curso-de-python\exercícios')
from ex108 import moedas

price = float(input('Digite o preço: R$'))
print(f'A metade de {price:.2f} é {moedas.metade(price):.2f}')
print(f'O dobro de {price:.2f} é {moedas.dobro(price):.2f}')
print(f'Aumentando 10%, temos {moedas.aumentar(price, 10):.2f}')
print(f'Reduzindo 13%, temos {moedas.diminuir(price, 13):.2f}')

