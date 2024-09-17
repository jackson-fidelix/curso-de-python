from datetime import datetime
ano = int(input('Digite seu ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - ano
if idade <= 9:
    print('A sua idade é {} anos e você é da CLASSE MIRIM!'.format(idade))
elif idade > 9 and idade <= 14:
    print('A sua idade é {} anos e você é da CLASSE INFANTIL!'.format(idade))
elif idade > 14 and idade <= 19:
    print('A sua idade é {} anos e você é da CLASSE JUNIOR!'.format(idade))
elif idade == 20:
    print('A sua idade é {} anos e você é da CLASSE SÊNIOR!'.format(idade))
else:
    print('A sua idade é {} anos e você é da CLASSE MASTER!'.format(idade))