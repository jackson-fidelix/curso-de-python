preco_produto = float(input('Digite o preço do produto: '))
print('===--===--===--===--===--===--===--===--===')
print('ESCOLHA A FORMA DE PAGAMENTO:')
print('1 - PARA MODALIDADE À VISTA')
print('2 - PARA MODALIDADE À VISTA NO CARTÃO')
print('3 - PARA MODALIDADE ATÉ 2X NO CARTÃO')
print('4 - PARA MODALIDADE 3X OU MAIS NO CARTÃO')
print('===--===--===--===--===--===--===--===--===')
escolha = int(input('Qual a opção escolhida: '))
if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
    print('Opção inexistente!')
else:
    if escolha == 1:
        novo_preco = preco_produto - (preco_produto * 0.10)
        print('Você escolheu a modalidade À VISTA e terá 10% de desconto.'
              ' O valor de sua compra agora é de R${:.2f}'.format(novo_preco))
    elif escolha == 2:
        novo_preco = preco_produto - (preco_produto * 0.05)
        print('Você escolheu a modalidade À VISTA NO CARTÃO e terá 5% de desconto.'
              ' O valor de sua compra agora é de R${:.2f}'.format(novo_preco))
    elif escolha == 3:
        total  = preco_produto
        parcela = total / 2
        print('Você escolheu a modalidade 2x NO CARTÃO, 2x de R${:.2f} .' 
              ' O valor total de sua compra ainda é de R${:.2f}'.format(parcela, preco_produto))
    else:
        novo_preco = preco_produto + (preco_produto * 0.20)
        print('Você escolheu a modalidade 3x OU MAIS NO CARTÃO e terá 20% de juros.'
              ' O valor de sua compra é de R${:.2f}'.format(novo_preco))

