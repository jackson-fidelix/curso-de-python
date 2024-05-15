preco = float(input('Digite o preço do produto: '))
taxa_promo = float(preco * 0.05)
promo = float(preco - taxa_promo)
print('O valor do produto na PROMOÇÃO é de R${:.2f}! \n'
      'Nessa promoção consideramos uma taxa de desconto de 5%. \n'
      'O valor de desconto foi de R${:.2f}!'.format(promo, taxa_promo))