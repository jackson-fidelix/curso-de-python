frase = 'Curso em Vídeo Python'
# print(frase[3:13])
#print(frase[::2])
#print('Oi')
#print(""""Esse é um texto imenso que foi testado para ser postado sem o uso de vários prints
#Esse é um texto imenso que foi testado para ser postado sem o uso de vários prints
#Esse é um texto imenso que foi testado para ser postado sem o uso de vários prints""")

#print(frase.upper().count('O'))
#print(len(frase))
#print(frase.replace('Python', 'Jacksudo'))
#lembrando que a string é imutável, com replace seria algo pontual, naquela instância de teste

#print(frase.lower().find('vídeo'))

print(frase.split())
#divide a lista de acordo com seus espaços
dividido = frase.split()
print(dividido[2][3])
#basicamente seria pega o divido 2 que é Vídeo e me dê a letra 3 que seria E [0,1,2,3,4]
