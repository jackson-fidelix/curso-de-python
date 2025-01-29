#Adicione ao módulo moedas.py criado nos desafios anteriores uma função chamada
#resumo(), que mostre na tela algumas funções geradas pelas funç~pes que 
#já temos no módulo criado até aqui
import sys
sys.path.append('e:\MeusProjetos\curso-de-python\exercícios')
from ex110 import moedas

price = float(input('Digite o preço: R$'))
moedas.resumo(price, 80, 35)
# print(f'A metade de {moedas.moeda(price)} é {moedas.metade(price, False)}')
# print(f'O dobro de {moedas.moeda(price)} é {moedas.dobro(price, True)}')
# print(f'Aumentando 10%, temos {moedas.aumentar(price, 10, True)}')
# print(f'Reduzindo 13%, temos {moedas.diminuir(price, 13, True)}')

