numbers = input('Digite um número de 0 a 9999: ')
newnumbers = list(numbers)
print('Unidade:', numbers[3] if len(numbers) > 0 else '0')
print('Dezena:', numbers[2] if len(numbers) > 0 else '0')
print('Centena:', numbers[1] if len(numbers) > 0 else '0')
print('Milhar:', numbers[0] if len(numbers) > 0 else '0')
