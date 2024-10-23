#Criando um Menu de Opções
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
escolha = 99
while escolha != 5:
    print('=---'*8)
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos Números')
    print('[5] - Sair do Programa')
    print('=---'*8)
    escolha = int(input('Qual é a sua escolha? '))
    if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5:
        print('Opção INVÁLIDA...Tente novamente!')  
    elif escolha == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}!')
    elif escolha == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}!')
    elif escolha == 3:
        if n1 > n2:
            print(f'O número maior é {n1}!')
        elif n2 > n1:
            print(f'O número maior é {n2}!')
        else:
            print('Os números são iguais, portanto não há um MAIOR!')
    elif escolha == 4:
        n1 = int(input('Digite o novo valor do 1° número: '))
        n2 = int(input('Digite o novo valor do 2° número: '))
print('Você saiu do programa com sucesso!!!')
print('Obrigado por utilizar nosso sistema de MENUs!')
