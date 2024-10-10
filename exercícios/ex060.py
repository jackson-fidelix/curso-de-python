num = int(input('Digite um número qualquer: '))
fatorial = 1
fatores = []

while num > 0:
    fatorial *= num
    fatores.append(str(num))
    num -= 1    

print(' x '.join(fatores), end=" = ")
print(f'{fatorial}')