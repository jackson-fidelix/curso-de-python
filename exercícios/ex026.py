frase = input('Digite uma frase qualquer: ').strip()
novafrase = frase.upper()
letra = 'A'
quantidadeA = novafrase.count(letra)
print('A frase digitada contém {} letras A!'.format(quantidadeA))

primeira_posicao = novafrase.find(letra)
print('A primeira vez que a letra "A" apareceu foi no Índice {}!'.format(primeira_posicao))
ultima_posicao = novafrase.rfind(letra)
print('A última vez que a letra "A" apareceu foi no Índice {}!'.format(ultima_posicao))