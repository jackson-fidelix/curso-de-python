def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == "":     
            print(f'\033[mErro: "{entrada}" não é um preço válido!\033[m')
        else:
            válido = True
            return float(entrada)
