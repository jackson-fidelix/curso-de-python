distancia = int(input('Digite a distância de sua viagem em KM: '))
if distancia <= 200:
    distancia_curta = distancia * 0.50
    print('O valor cobrado por KM de sua viagem é de R$ 0,50, pois ela é uma viagem CURTA. Você pagará um total de R${:.2f}!'.format(distancia_curta))
else:
    distancia_longa = distancia * 0.45
    print('O valor cobrado por Km de sua viagem é de R$ 0,45, pois ela é uma viagem LONGA. Você pagará um total de R${:.2f}!'.format(distancia_longa))