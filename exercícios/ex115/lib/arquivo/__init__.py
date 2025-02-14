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
        #coloque o caminho onde deseja criar o arquivo
        caminho = r'e:/MeusProjetos/curso-de-python/exercícios/ex115/dados.txt'
        a = open(caminho, 'x')
        a.close()
    except FileExistsError:
        print(f'\033[7;32m O arquivo {nome} já existe! \033[m')
    except:
        print('Houve algum ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(caminho):
    try:
        #coloque o caminho onde o arquivo está localizado
        caminho = r'e:/MeusProjetos/curso-de-python/exercícios/ex115/dados.txt'
        a = open(caminho, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        #coloque o caminho onde o arquivo está localizado
        caminho = r'e:/MeusProjetos/curso-de-python/exercícios/ex115/dados.txt'
        a = open(caminho, 'at')
    except:
        print(f'Houve um ERRO na abertura do arquivo {arq}!')
    else:
        print('Arquivo aberto.')
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na inserção dos dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close
