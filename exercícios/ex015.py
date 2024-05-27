dias = int(input('Quantos dias você alugou esse carro? '))
km = float(input('Quantos Km você andou com esse carro? '))
valor_dias = dias * 60
valor_km = km * 0.15
print('Com base na quantidade de dias e km informados, o total a pagar pela locação é R${:.2f}!'.format(valor_dias+valor_km))
