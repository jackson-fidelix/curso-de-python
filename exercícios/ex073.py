#crie uma tupla com os 20 primeiros colocados da Tabela do Brasileirão, na ordem da colocação 2024-11-14. Mostre:
#A) O G5
#B) O Z4
#C) Uma lista dos times em ordem alfabética
#D) Em que posição o VERDÃO está

time_brasileiro2024 = ('Botafogo','Palmeiras', 'Fortaleza', 'Flamengo', 'Internacional', 'São Paulo', 'Cruzeiro', 'Bahia', 'Vasco', 'Atlético-MG', 'Corinthians', 'Grêmio', 'Vitória', 'Fluminense', 'Criciúma', 'Juventude', 'Bragantino', 'Athletico-PR', 'Cuiabá', 'Atlético-GO')

print(f'Os 5 primeiros colocados do Brasileirão 2024 são: \n{time_brasileiro2024[0:5]}')
print('===-==='*10)
print(f'Os 4 últimos colocados são: \n{time_brasileiro2024[-4:]} ')
print('===-==='*10)
print(f'A classificação em Ordem Alfabética seria: \n{sorted(time_brasileiro2024)}')
print('===-==='*10)
print(f'O VERDÃO está na posição: {time_brasileiro2024.index('Palmeiras')+1}')
print('===-==='*10)



