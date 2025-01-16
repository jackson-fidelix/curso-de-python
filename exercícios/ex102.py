#crie um programa que tenha um função fatorial() que receba dois parâmetros:
#o primeiro que indique um número a calcular e o outro chamado show, que será
#(opcional) indicando se será mostrado ou não na tela o processo de 
#cálculo do fatorial

def fatorial(num, show = False):
    """
    -> Calcula o Fatorial de um número
    :param. n: O número a ser calculado
    :param. show: (opcional) Mostrar ou não a conta
    :return: O valor fatorial de um número n
    """
    fat = 1
    numbers = []

    while  num != 0:
        fat = fat * num
        #join funciona apenas com strings, portanto preciso converter
        numbers.append(str(num)) 
        num -= 1
    if show:
        print(" x ".join(numbers), "=", fat)
    else:
        print(fat)
    
    return fat

print("---"*15)
resultado = fatorial(7, True)
print(f'O Fatorial retornado: {resultado}.')
other_result = fatorial(10)
print(f'O Fatorial retornado: {other_result}.')
another_result = fatorial(3, True)
print(f'O Fatorial retornado: {another_result}.')
help(fatorial)