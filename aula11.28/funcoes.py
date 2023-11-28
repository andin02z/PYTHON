# faça uma função que retotne o reverso de um numero inteiro informado. por exemplo: 127-> 721
def numero_reverso (numero):
    reverso = 0
    while numero > 0:
        #pegar o ultimo valor do numero 
        ultimo_valor = numero % 10

        # add ultimo valor
        reverso = (reverso * 10) + ultimo_valor


        # tira ultimo valor
        numero = numero // 10
        # retorna o reverso
 
numero = int(input('informe um numero : '))
resultado = ...
print(f'o numero informado ')

