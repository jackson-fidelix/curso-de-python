#Crie um program que tenha uma função leiaint(), que vai funcionar 
#de forma semelhante à função input() do Python, só que fazendo
#a validação para aceitar apenas um valor numérico.

def leiaInt(msg):
    # ok = False
    # valor = 0
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('\033[1;31mERROR! Digite um número inteiro.\033[m')
    #outra forma, sem o try
    #n = str(input(msg))
        # if n.isnumeric():
        #     valor = int(n)
        #     ok = True
        # else:
        #     print('\033[1;31mERROR! Digite um número inteiro.\033[m')
    #   if ok:
    #       break
    #return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
