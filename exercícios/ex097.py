#Faça um comando que tenha uma função chamada escreva(), que receba
#um texto qualquer como parâmetro e mostre uma mensagem,
#com tamanho adaptável. 

def escreva(word):
    tam = len(word) +4
    print('-' * tam)
    print(f'  {word}')
    print('-' * tam)

escreva(' Teste um, dois, três...   ')
escreva(' Jackson Felipe Fidelix   ')
escreva(' Funções em Python -  Aprendendo!   ')
