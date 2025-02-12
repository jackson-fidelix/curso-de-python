# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo
# seu nome e idade em um arquivo de texto simples. O sistema só vai ter 
# 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

import sys
import os
# coloque o caminho do seu projeto, provavelmente será diferente do meu
sys.path.append(r'e:\MeusProjetos\curso-de-python\exercícios')
from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'dados.txt'

if not arquivoExiste(arq):
    print('Arquivo não encontrado!')
    criarAquivo(arq)
else:
    print('Arquivo encontrado...')
    #onde esta o arquivo?  >>> print(f"Arquivo criado em: {os.path.abspath(arq)}")

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho(f'Opção {resposta} selecionada')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(2)