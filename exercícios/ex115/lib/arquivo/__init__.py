from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarAquivo(nome):
    try:
        caminho = r'e:/MeusProjetos/curso-de-python/exercícios/ex115/dados.txt'
        a = open(caminho, 'wt+')
        a.close()
    except:
        print('Houve algum ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(caminho):
    try:
        caminho = r'e:/MeusProjetos/curso-de-python/exercícios/ex115/dados.txt'
        a = open(caminho, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.readlines())