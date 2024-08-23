vel = int(input('Digite sua velocidade: '))
if vel <= 80:
    print('Muito bem, você é um motorista prudente e está andando na velocidade correta!')
else:
    vel_diferenca = vel - 80
    vel_multa = vel_diferenca * 7
    print('Você foi multado por excesso de velocidade!')
    print('Sua velocidade é {}Km acima do permitido, por isso deve pagar uma multa de R${},00!'.format(vel_diferenca, vel_multa))

