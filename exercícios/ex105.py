#Faça um programa que tenha uma função notas() que pode receber várias notas 
#de alunos e vai retornar um dicionário com as seguintes informações:
#Quantidade de notas
#A maior nota
#A média da turma
#A situação(opcional)

def notas(* notas, sit = False):
    """
    ->Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos(aceita várias)
    :param sit: vaçor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    resp = {}
    resp['total'] = len(notas)
    resp['maior'] = max(notas)
    resp['menor'] = min(notas)
    resp['média'] = sum(notas) / len(notas)

    if sit == True:
        if resp['média'] > 7:
            resp['situação'] = 'BOA'
        elif resp['média'] >= 5:
            resp['situação'] = 'RAZOÁVEL'
        else:
            resp['situação'] = 'RUIM' 
    return resp


resp = notas(10, 6, 5, sit=True)
print(resp)
help(notas)
