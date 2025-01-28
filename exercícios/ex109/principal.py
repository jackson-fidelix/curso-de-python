#Modifique as funções que foram criadas no desafio 107 para que elas aceitem
#um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
#formatado pela função moeda(), desenvolvida no desafio 108
import sys
sys.path.append('e:\MeusProjetos\curso-de-python\exercícios')
from ex109 import moedas

price = float(input('Digite o preço: R$'))
print(f'A metade de {moedas.moeda(price)} é {moedas.metade(price, False)}')
print(f'O dobro de {moedas.moeda(price)} é {moedas.dobro(price, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(price, 10, True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(price, 13, True)}')

