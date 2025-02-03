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
    print('-'*35)
    print('RESUMO DO VALOR'.center(35))
    print('-'*35)
    print(f'{'Preço analisado:'} \t{moeda(preco)}')
    print(f'{'Dobro do preço:'} \t{moeda(preco * 2)}')
    print(f'{'Metade do preço:'} \t{moeda(preco / 2)}')
    print(f'{aumento}% de aumento: \t{moeda(aumentar(preco, aumento))}')
    print(f'{desconto}% de redução: \t{moeda(diminuir(preco, desconto))}')
    print('-'*35)
