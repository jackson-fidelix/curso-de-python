nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = float((nota1 + nota2)/2)
print('A primeira nota foi \033[1;34m{}\033[m e a segunda \033[1;36m{}\033[m, a média das notas é \033[1;33m{}\033[m!'.format(nota1, nota2, media))
