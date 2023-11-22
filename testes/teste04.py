maior = 0
menor = 0


while True:
    saida = input('digite "S" para sair: ')
    if saida == 's' or saida == 's' :
        print('volte sempre !')
        break

    numero = int(input('informe um numero inteiro '))

    if numero > maior:
        maior = numero 
    if numero == menor or numero < menor :
        menor = numero 


print(f' A soma de {maior} + { menor } = {menor} + {maior }')
print(f' o maior valor é: { maior}')
print(f' o menor valor é: { menor }')