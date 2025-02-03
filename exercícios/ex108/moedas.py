def aumentar(p, n):
    aumento = p + (p * n / 100)
    return aumento


def diminuir(p, n):
    reducao = p - (p * n / 100)
    return reducao 


def dobro(p):
    resposta = p *2
    return resposta


def metade(p):
    res = p / 2
    return res


def moeda(p):
    return f'R${p:>.2f}'.replace('.', ',')

