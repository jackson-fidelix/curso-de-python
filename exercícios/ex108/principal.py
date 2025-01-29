#Adapte o código do desafio 107, criando uma função adicional chamada  
#moeda() que consiga mostrar os valores coomo um valor monetário formatado 
import sys
sys.path.append('e:\MeusProjetos\curso-de-python\exercícios')
from ex108 import moedas

price = float(input('Digite o preço: R$'))
print(f'A metade de {moedas.moeda(price)} é {moedas.moeda(moedas.metade(price))}')
print(f'O dobro de {moedas.moeda(price)} é {moedas.moeda(moedas.dobro(price))}')
print(f'Aumentando 10%, temos {moedas.moeda(moedas.aumentar(price, 10))}')
print(f'Reduzindo 13%, temos {moedas.moeda(moedas.diminuir(price, 13))}')
