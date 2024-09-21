#desenvolver uma PA e somar os 10 primeiros números
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
soma_pa = 0
for i in range(10):
    termo_atual = primeiro_termo + i * razao
    soma_pa += termo_atual
    print(termo_atual)
print('A soma da PA é de {}'.format(soma_pa))