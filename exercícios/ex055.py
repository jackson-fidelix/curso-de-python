#leia o peso de 5 pessoas e mostre qual o maior e qual o menor
peso_maior = 0
peso_menor = 0 
for i in range(1, 5+1):
    peso = float(input('Digite seu peso: '))
    novo_peso = peso
    if peso_maior == 0 or novo_peso > peso_maior:
        peso_maior = novo_peso
        if peso_menor == 0:
            peso_menor = peso_maior
    elif novo_peso < peso_menor:
        peso_menor = novo_peso
print(f'O peso maior é  {peso_maior :.2f} Kg e o menor é {peso_menor :.2f} Kg!')
