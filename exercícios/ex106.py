#Faça um mini-programa que utilize o Interactive Help do Python. O usuário
#vai digitar o comando e o manual vai aparecer. Quando o usuário digitar 
#a palavra 'FIM', o programa se encerrará. OBS: Use cores.
from time import sleep

c = {
    0: '\033[m',            # 0 - sem cores
    1: '\033[0;30;41m',     # 1 - vermelho
    2: '\033[0;30;42m',     # 2 - verde
    3: '\033[0;30;43m',     # 3 - amarelo
    4: '\033[0;30;44m',     # 4 - azul
    5: '\033[0;30;45m',     # 5 - roxo
    6: '\033[7;40m'         # 6 - branco
}



def ajuda(comando):
    titulo(f"Acessando o manual do comando \'{user}\'", 4)
    print(c[6])
    help(comando)
    print(c[0])
    sleep(2)


def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor])
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0])
    sleep(1)


user = ""
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    user = str(input('Função ou Biblioteca > '))
    if user.upper() == 'FIM':
        break
    else:
        ajuda(user)
titulo('ATÉ LOGO', 1)
