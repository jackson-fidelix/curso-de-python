#melhorar o exercício 61 sobre PA
primeiro_termo = int(input('1° Termo: '))
razao = int(input('Razão: '))
i = 0
soma_pa = 0
termos = []
quant_termos = 10

while i != quant_termos:
    termo_atual = primeiro_termo + razao * i
    soma_pa += termo_atual
    print(f'{termo_atual} ', end="| ") 
    termos.append(str(termo_atual))
    i += 1

while True:
    termos_extras = int(input('\n Deseja mostrar mais quantos termos? '))
    if termos_extras == 0:
        break
    quant_termos +=  termos_extras
    while i != quant_termos:
        termo_atual = primeiro_termo + razao * i
        soma_pa += termo_atual
        print(f'{termo_atual} ', end="| ") 
        termos.append(str(termo_atual))
        i += 1

print('===#'* (quant_termos + 5))
print(f'Esses são os {quant_termos} primeiros termos da PA: ')
print(' → '.join(termos))
print(f'Sua soma é de {soma_pa}!')
print('===#'* (quant_termos + 5))