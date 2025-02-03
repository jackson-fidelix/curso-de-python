def aumentar(p, n, situacao = False):
    aumento = p + (p * n / 100)
    if situacao == True:
        return moeda(aumento)
    return aumento


def diminuir(p, n, situacao = False):
    reducao = p - (p * n / 100)
    if situacao:
        return moeda(reducao)
    return reducao 


def dobro(p, situacao = False):
    if situacao:
        return moeda(p * 2)
    return p * 2


def metade(p, situacao = False):
    if situacao:
        return moeda(p / 2)
    return p / 2


def moeda(p):
    return f'R${p:.2f}'.replace('.', ',')

def resumo(preco, aumento, desconto):
    print('---'*10)
    print('RESUMO DO VALOR'.center(30))
    print('---'*10)
    print(f'Preço analisado: {moeda(preco):>12}')
    print(f'Dobro do preço: {moeda(preco * 2):>14}')
    print(f'Metade do preço: {moeda(preco / 2):>12}')
    print(f'{aumento}% de aumento: {moeda(aumentar(preco, aumento)):>13}')
    print(f'{desconto}% de redução: {moeda(diminuir(preco, desconto)):>13}')
    print('---'*10)

