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
    resp = p * 2
    if situacao:
        return moeda(resp)
    return resp


def metade(p, situacao = False):
    res = p /2
    if situacao:
        return moeda(res)
    return res


def moeda(p):
    return f'R${p:.2f}'.replace('.', ',')

