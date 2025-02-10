# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo
# seu nome e idade em um arquivo de texto simples. O sistema só vai ter 
# 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

import sys
# coloque o caminho do seu projeto, provavelmente será diferente do meu
sys.path.append('e:\MeusProjetos\curso-de-python\exercícios')
from ex115.lib.interface import *

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        print(f'Opção {resposta} selecionada')
    elif resposta == 2:
        print(f'Opção {resposta} selecionada')
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')