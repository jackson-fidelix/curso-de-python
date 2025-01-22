#Faça um mini-programa que utilize o Interactive Help do Python. O usuário
#vai digitar o comando e o manual vai aparecer. Quando o usuário digitar 
#a palavra 'FIM', o programa se encerrará. OBS: Use cores.

def ihpython(user = ""):
    user == 'Início'
    while user != "FIM":
        msg_welcome = 'SISTEMA DE AJUDA PyHELP'
        tam_welcome = len(msg_welcome) + 4
        print('\033[7;32m')
        print('~' * tam_welcome)
        print('  SISTEMA DE AJUDA PyHELP')
        print('~' * tam_welcome)
        print('\033[m')

        user = str(input('Função ou Biblioteca > '))
        if user in "FimFinalizarfimFIM":
            end = 'ATÉ LOGO'
            tam_end = len(end) + 4
            print('\033[7;31m')
            print('~' * tam_end)
            print('  ATÉ LOGO')
            print('~' * tam_end)
            print('\033[m')
            break
        else:
            msg_access = f"Acessando o manual do '{user}'..."
            tam_acces = len(msg_access) + 4
            print('\033[7;34m')
        print('~' * tam_acces)
        print(f"Acessando o manual do '{user}'...")
        print('~' * tam_acces)
        print('\033[m')

        print('\033[7m')
        print(help(user))
        print('\033[m')


user = "iniciar"
ihpython(user)
