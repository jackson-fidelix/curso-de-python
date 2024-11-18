"""crie um programa que tenha uma tupla com diversas palavras(sem acentos), 
depois mostre quais vogais existem em cada palavra"""

words = ('orar', 'louvar', 'jejuar', 'cantar', 'interceder', 'ler', 'adorar', 'falar', 'servir', 'testemunhar',
         'curar', 'libertar', 'aprender', 'ensinar', 'amar')

vogais = 'aeiou'

for verbos in words:
    vogais_encontradas = []
    for letra in verbos:
        if letra in vogais:
            vogais_encontradas.append(letra)
    if vogais_encontradas:
        print(f'A palavra {verbos.upper()} contém as vogais: {', '.join(vogais_encontradas)}')
    else:
        print(f'A palavra {verbos.upper()} não contém vogais!')
