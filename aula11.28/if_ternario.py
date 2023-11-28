# a condição ternaria acontece em formato de linha 
salario = int(input('informe o valor do seu salario '))
if salario >= 2500.00:
    print("IR sera cobrado")
else:
    print('ir não sera cobrado')

variavel_controle = 'IR sera cobrado' if salario >= 2500.00 else 'IR não sera cobrado '
print(variavel_controle)
