#números da sequência de FIBONACCI
escolha = int(input('Quantos números da sequência de FIBONACCI você quer imprimir? '))
termos_fibonacci = [0, 1]

while len(termos_fibonacci) < escolha:
    proximo_termo = termos_fibonacci[-1] + termos_fibonacci[-2]
    termos_fibonacci.append(proximo_termo)

print(f'Abaixo segue os \033[1;31m{escolha}\033[m primeiros termos de FIBONACCI: ')
print(f'\033[1;32m {termos_fibonacci[:escolha]} \033[m')