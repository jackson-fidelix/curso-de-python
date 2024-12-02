# Crie um programa onde o usuário digite uma expressão qualquer que
# use parênteses, Seu aplicativo deverá analisar se a expressão passada
# está com parênteses abertos e fechados na ordem correta.

frase = str(input('Digite uma expressão: '))
pilha = []
for simb in frase:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\033[1;32mEssa expressão está correta!\033[m')
else:
    print('\033[1;31mSua expressão está errada!\033[m')
    print(pilha)