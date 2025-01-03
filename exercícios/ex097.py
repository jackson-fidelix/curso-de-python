#Faça um comando que tenha uma função chamada escreva(), que receba
#um texto qualquer como parâmetro e mostre uma mensagem,
#com tamanho adaptável. 

def escreva(word):
    print('-' * len(word))
    print(f' {word} ')
    print('-' * len(word))

escreva(' Teste um, dois, três...   ')
escreva(' Jackson Felipe Fidelix   ')
escreva(' Funções em Python -  Aprendendo!   ')
