#descobrindo se uma frase é um palíndromo com FOR
frase = str(input('Digite uma frase qualquer: ')).upper()
nova_frase = frase.replace(' ', '')
invertida = ''
for letra in range(len(nova_frase)-1, -1, -1):
    invertida += nova_frase[letra]

if invertida == nova_frase:
    print('A frase {} é um PALÍNDROMO!'.format(frase))
else:
    print('Essa frase NÃO É um palíndromo!')
