# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
# agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

import sys
sys.path.append('e:\MeusProjetos\curso-de-python\exercícios')
from ex113.dados import leiaFloat
from ex113.dados import leiaInt

n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real {n2}')