# Crie um programa onde o usuário digite uma expressão qualquer que
# use parênteses, Seu aplicativo deverá analisar se a expressão passada
# está com parênteses abertos e fechados na ordem correta.

frase = str(input('Digite uma expressão: '))
for letra in frase:
    quant_aberto = frase.count('(')
    quant_fechado = frase.count(')')

if quant_aberto == quant_fechado:
    print('\033[1;32mEssa expressão está correta!\033[m')
else:
    print(f'Sua expressão está errada, pois contém \033[1;31m{quant_aberto} "(" parênteses abertos\033[m e \033[1;31m{quant_fechado} ")" fechados\033[m')
