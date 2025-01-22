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
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(' x ',end="")
            else:
                print(' = ', end="")
        fat *= c
    return fat

    #segunda forma de fazer
    # numbers = []
    # while  num != 0:
    #     fat = fat * num
    #     #join funciona apenas com strings, portanto preciso converter
    #     numbers.append(str(num)) 
    #     num -= 1
    # if show:
    #     print(" x ".join(numbers), "=", fat)
    # else:
    #     print(fat)   
    # return fat
    

print("---"*16)
print(fatorial(5, True))
print(fatorial(10))
print(fatorial(3, True))
help(fatorial)
print("---"*16)