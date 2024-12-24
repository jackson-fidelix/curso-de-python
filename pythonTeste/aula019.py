pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':'23'}
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos!')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

#del pessoas['sexo']
pessoas['nome'] = 'Jack Tech'
pessoas['peso'] = 88
for k in pessoas.keys():
    print(k)
print('---'*2)
for k in pessoas.values():
    print(k)
print('---'*2)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('---'*10)
brasil = []
estado1 = {'uf':'São Paulo', 'sigla':'SP'}
estado2 = {'uf':'Santa Catarina', 'sigla':'SC'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['sigla'])
print('---'*10)
estado = dict()
brasil = list()
for i in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
    print()
print('---'*10)
    #ou, podemos fazer:
for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()
