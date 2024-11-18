""" Crie um programa que tenha uma tupla única com nomes de produtos 
e seus respectivos preços, na sequência. No final, mostre uma listagem
de preços, organizando os dados em forma tabular. """

dados = ('Processador', '1750,00', 'Placa de Vídeo', '2399,00', 'Monitor', '999,99', 'Mouse Gamer', '299,00',
         'Teclado Gamer', '399,00', 'Mousepad', '29,99', 'Headset', '1099,00', 'Cadeira Gamer', '499,99')

print("==="*15)
print('LISTAGEM DE PREÇO'.center(45))
print("==="*15)
print('PRODUTO'.center(30), end="")
print('PREÇO'.rjust(10))
print("---"*15)
for i in range(0, len(dados),2):
    produto = dados[i]
    preco = dados[i+1]
    print(f"{produto:.<30}", end=" | ")
    print(f"R$ {preco:>8}")
print("---"*15)
