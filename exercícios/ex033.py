numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro numero: '))
if numero1 < numero2 & numero2 < numero3:
    print('O MENOR número é o {} e o MAIOR é o {}!(solução 1)'.format(numero1, numero3))
elif numero1 < numero2 and numero3 < numero2 and numero1 < numero3:
    print('O MENOR número é o {} e o MAIOR é o {}!(solução 1.2)'.format(numero1, numero2))
elif numero2 < numero3 and numero3 < numero1:
    print('O MENOR número é o {} e o MAIOR é o {}!(solução 2)'.format(numero2, numero1))
elif numero2 < numero1 and numero2 < numero3 and numero3 > numero1:
    print('O MENOR número é o {} e o MAIOR é o {}!(solução 2.2)'.format(numero2, numero3))
elif numero1 > numero2 and numero1 > numero3 and numero3 < numero2:
    print('O MENOR número é o {} e o MAIOR é o {}!(solução 3)'.format(numero3, numero1))
else:
    print('O MENOR número é o {} e o MAIOR é o {}!(solução 4)'.format(numero3, numero2))