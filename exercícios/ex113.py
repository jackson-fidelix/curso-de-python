# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
# agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while msg != int:
        try:
            n = int(input(msg))
            return n
        except (ValueError,TypeError):
            print(f'\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[1;31mERROR: O Usuário preferiu não digitar esse número.\033[m')
            n = 0
            break
    return n

def leiaFloat(msg):
    while msg != float:
        try:
            n = float(input(msg))
            return n
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número real válido\033[m')
        except KeyboardInterrupt:
            print(f'\033[1;31mERROR: O Usuário preferiu não digitar esse número.\033[m')
            n = 0
            break
    return n

        
n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real {n2}')
