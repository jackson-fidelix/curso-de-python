largura = float(input('Digite o valor de Largura da parede em m²: '))
altura = float(input('Digite o valor a Altura da parede em m²: '))
parede_inteira = (altura * largura)
tinta = float(2)
calculo_tinta = (parede_inteira / tinta)
print('Você precisará de {:.2f} litros de tinta para pintar a parede inteira. \n'
      'Sabendo que cada Litro pinta {:.2f}m² e a ÁREA total da parede é {:.2f}m²!'.format(calculo_tinta, tinta, parede_inteira))
