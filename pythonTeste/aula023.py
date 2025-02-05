# Tratamento de Erros e Exceções


# sintático - exceção

# "print(x)" nesse caso, x não foi iniciado anteriormente 
# n = int(input('Número: ')) #Digitei 'OITO'
# "print(n)" nesse caso, n não é um inteiro e apresenta ValueError
#ZeroDivisionError, no caso de divisões por 0, conforme o próprio nome

try: # operação
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: # falhou
    print(f'Infelizmente tivemos um problema :(.')
    print(f'O problema foi {erro.__class__}')
else: # deu certo
    print(f'O resultado é {r:.2f}')
finally: # certo / falhou - sempre vai acontecer
    print('Volte sempre, muito obrigado!')
