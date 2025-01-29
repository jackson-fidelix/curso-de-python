# Crie um pacote chamado utilizadesCeV que tenha dois módulos internos 
# chamados moeda e dado. Transfira todas as funções utilizadas nos 
# desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

import sys
sys.path.append('e:\MeusProjetos\curso-de-python\exercícios')
from ex111.utilidadesCeV import moeda


price = float(input('Digite o preço: R$'))
moeda.resumo(price, 80, 35)
