
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
    result = {}
    result['total'] = len(notas)
    result['maior'] = max(notas)
    result['menor'] = min(notas)
    result['média'] = sum(notas) / len(notas)

    if sit == True:
        if result['média'] >= 7:
            result['situação'] = 'BOA'
        elif result['média'] >= 5:
            result['situação'] = 'RAZOÁVEL'
        else:
            result['situação'] = 'RUIM' 
    return result


resp = notas(10, 6, 5, sit=True)
print(resp)
