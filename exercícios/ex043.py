peso = float(input('Digite seu peso atual: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.2f} e você está Abaixo do Peso!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.2f} e você está no Peso Ideal!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f} e você está Sobrepeso!'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é {:.2f} e você está com Obesidade!'.format(imc))
else:
    print('Seu IMC é {:.2f} e você está com Obesidade Mórbida!'.format(imc))