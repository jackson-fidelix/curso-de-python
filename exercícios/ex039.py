from datetime import date
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade < 18:
    saldo = ano_atual + (18 - idade)
    print('Você é muito jovem, possui {} aninhos... Faltam {} anos para seu alistamento!'.format(idade, 18-idade))
    print('O ano atual é {} e você se alistará em {}!'.format(ano_atual, saldo))
elif idade == 18:
    print('Parabéns, você completou a maioridade e agora está na hora de se alistar, pois possui {} anos!'.format(idade))
else:
    alistamento = ano_atual - (idade - 18)
    print('Não perca mais tempo!!\n'
          'Você possui {} anos e já passou {} anos do prazo de alistamento!'.format(idade, idade-18))
    print('O ano atual é {} e você se alistou em {}!'.format(ano_atual, alistamento))