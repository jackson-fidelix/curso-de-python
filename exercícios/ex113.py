# Reescrewva a função leiaInt() que fizemos no desafio 104, incluindo
# agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print(f'\033[1;31mERROR: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[1;31mERROR: O Usuário preferiu não digitar esse número.\033[m')
            n = 0
            break
        else:


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
