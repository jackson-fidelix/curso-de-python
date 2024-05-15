largura = int(input('Digite o valor de Largura da parede em m²: '))
altura = int(input('Digite o valor a Altura da parede em m²: '))
parede_inteira = int(altura * largura)
tinta = int(2)
calculo_tinta = int(parede_inteira / tinta)
print('Você precisará de {} litros de tinta para pintar a parede inteira. \n'
      'Sabendo que cada Litro pinta {}m² e a ÁREA total da parede é {}m²!'.format(calculo_tinta, tinta, parede_inteira))
