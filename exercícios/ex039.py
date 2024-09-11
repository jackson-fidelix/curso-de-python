from datetime import datetime
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
if idade < 18:
    print('Você é muito jovem, possui {} aninhos... Faltam {} anos para seu alistamento!'.format(idade, 18-idade))
elif idade == 18:
    print('Parabéns, você completou a maioridade e agora está na hora de se alistar, pois possui {} anos!'.format(idade))
else:
    print('Não perca mais tempo!!\n'
          'Você possui {} anos e já passou {} anos do prazo de alistamento!'.format(idade, idade-18))