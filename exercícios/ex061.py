#melhorar o exercício 51 sobre PA
primeiro_termo = int(input('1° Termo: '))
razao = int(input('Razão: '))
i = 0
soma_pa = 0
termos = []

while i != 10:
    termo_atual = primeiro_termo + razao * i
    soma_pa += termo_atual 
    termos.append(str(termo_atual))
    i += 1

print('===#'*12)
print('Esses são os 10 primeiros termos da PA: ')
print(' → '.join(termos))
print(f'Sua soma é de {soma_pa}!')
print('===#'*12)