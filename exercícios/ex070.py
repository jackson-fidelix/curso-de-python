#leia nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# qual o total de gasto, quantos produtos custam mais de R$1000 e qual o nome do produto mais barato
prices_sum = 0
expensive_product = 0
cheaper_price = 0
cheaper_name = ''

print('--*'*10)
print('\033[1;32mJACK TECH STORE\033[m'.center(40))
print('--*'*10)

while True:
    product = str(input('Nome do produto: ')).capitalize()
    price = float(input('Valor do Produto: R$'))
    prices_sum += price
    if price > 1000:
        expensive_product += 1
    if cheaper_price == 0:
        cheaper_price =  price
        cheaper_name = product
    elif price < cheaper_price:
        cheaper_price =  price
        cheaper_name = product
    print('\033[1;34m---\033[m'*10)
    register_product = str(input('Deseja continuar? [S/N]')).upper().strip()
    print('\033[1;34m---\033[m'*10)
    if register_product == 'S':
        continue
    elif register_product == 'N':
        break
    else:
        print('Opção inválida!')
    
print(f'O o total de gastos é R$\033[1;31m{prices_sum:.2f}\033[m!')
print(f'Existem \033[4;33m{expensive_product}\033[m produtos que custam mais de R$1000,00!')
print(f'O produto mais barato é \033[1;32m{cheaper_name}\033[m e ele custa R$\033[1;32m{cheaper_price:.2f}\033[m!')