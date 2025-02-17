# Crie um código em Python que teste se o site Pudim está acessível
# pelo computador usado.

import requests
import webbrowser

try:
    online = requests.get('https://www.pudim.com.br/')
    if online:
        print('\033[1;32mConsegui acessar o site Pudim com sucesso!\033[m')
        webbrowser.open('https://www.pudim.com.br/')
except:
    print('\033[1;31mO site Pudim não está acessível no momento\033[m')
