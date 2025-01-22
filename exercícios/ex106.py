#Faça um mini-programa que utilize o Interactive Help do Python. O usuário
#vai digitar o comando e o manual vai aparecer. Quando o usuário digitar 
#a palavra 'FIM', o programa se encerrará. OBS: Use cores.
c = {
    0: '\033[m',           # 0 - sem cores
    1: '\033[0;30;41m'     # 1 - vermelho
}


def ajuda(comando):
    help(comando)
    

def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end="")
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end="")


user = ""
while True:
    titulo('  SISTEMA DE AJUDA PyHELP', 1)
    user = str(input('Função ou Biblioteca > '))
    if user.upper() == 'FIM':
        break
    else:
        ajuda(user)
titulo('  ATÉ LOGO', 1)
