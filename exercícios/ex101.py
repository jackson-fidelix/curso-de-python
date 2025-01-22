#crie um programa que tenha i,a função chamada "voto()" que vai receber como
#parâmetro o ano de nascimento de uma pessoa, retornando um valor literal 
#indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

def voto(year):
    from datetime import date
    
    age = date.today().year - year 
    if 16 <= age < 18 or age > 65:
        return f'Com {age} anos: VOTO OPCIONAL.'
    elif 18 <= age <= 65:
        return f'Com {age} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {age} anos: VOTO NEGADO.'
        
    
nasc = int(input('Em que ano você nasceu: '))
print(voto(nasc))