def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)



#Quarta explicação
#def contador(* núm):
    #for valor in núm:
    #    print(f' {valor} ', end="")
    #print('\n == FIM == ')
#   tam = len(núm)
#    print(f'Recebi os valores {núm} e são ao todo {tam} números!')


#contador(2, 1, 7)
#contador(8, 0)
#contador(4, 4, 7, 6, 2)


#Terceira explicação
#def soma(a, b):
#    soma = a + b
#    print(soma)

#se não explicitar, o primeiro valor vai para A e o segundo para B
#soma(4, 5)
#soma(8, 9)
# ou explicitar
#soma(a = 2, b = 1)
#soma(b = 4, a = 1)


#Segunda Explicação
#def título(txt):
#    print('-'*30)
#    print(txt)
#    print('-'*30)


#título('        CURSO EM VÍDEO  ')
#título('        APRENDA PYTHON  ')
#título('        JACKSON FIDELIX  ')
#-----------------------


#primeira explicação
#def lin():
#    print('-'*30)


#Programa Principal
#lin()
#print('        CURSO EM VÍDEO  ')
#lin()
#lin()  
#print('        APRENDA PYTHON  ')
#lin()
#lin()
#print('        APRENDA PYTHON  ')  
#lin()
#---------------------
