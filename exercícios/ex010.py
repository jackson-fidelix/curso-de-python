wallet = float(input('Digite quantos reais você tem em sua carteira neste exato momento: R$'))
#considerando cotação do dólar do dia 15/05/2024 a R$5.13
usd = float(wallet/5.13)
print('Com esse valor você conseguirá comprar U${:.2f} dólares, desonsidernado SPREAD e demais TAXAS.'.format(usd))
