def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[1;31mERRO: O usuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return n
    

def menu(lista):
        cabeçalho('MENU PRINCIPAL')
        c = 1
        for item in lista:
            print(f'\033[1;33m{c}\033[m - \033[1;34m{item}\033[m')
            c += 1
        opc = leiaInt('\033[1;32mSua opção:\033[m ')
        return opc
