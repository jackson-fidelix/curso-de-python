#crie um progama que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso mostre a listagem de números gerado e também qual é o maior e o menor.
from random import randint
from time import sleep

numbers_list = []
smaller = bigger = 0

for c in range(1, 6):
    random_numbers = randint(0, 10)
    sleep(1)
    print(f'Estou gerando o {c}º número!')
    numbers_list.append(random_numbers)
    if smaller == 0 and bigger == 0:
        smaller = random_numbers
        bigger = random_numbers
    elif random_numbers > bigger:
        bigger = random_numbers
    elif random_numbers < smaller:
        smaller = random_numbers

numbers_tuple = tuple(numbers_list)

print(f'A tupla criada aleatoriamente é: {numbers_tuple}')
print(f'O maior número gerado é: {bigger}')
print(f'O menor número gerado é: {smaller}')
