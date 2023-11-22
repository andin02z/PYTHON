

numero = int(input('favor informar um numero inteiro :'))
intervalo = range(1, numero+1)
contador = 0
for i in intervalo:
    if numero % i == 0:
        print(f'foi divisivel por { i }')
        contador += 1
if contador == 2:
    print(f'o numero { numero } é primo ')