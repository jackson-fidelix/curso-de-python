sexo = 'letra'
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite a INICIAL do seu sexo: ')).upper().strip() [0]
    if sexo != 'F' and sexo != 'M':
        print('Você digitou a letra ERRADA!')
    elif sexo == 'F':
        print(f'Você digitou a letra "{sexo}", você é uma Mulher!')
    elif sexo == 'M':
        print(f'Você digitou a letra "{sexo}", você é um ALFA!')
print('FIM!')