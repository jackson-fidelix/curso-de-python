n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A sua média foi {:.2f}'.format(media))
if media >=7:
    print('Você foi aprovado!')
else:
    print('Burraldo, estude mais!')