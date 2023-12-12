frase = input("digite uma frase: ").split()
print()
print(frase)


while len(frase) < 10:
    frase = input("digite uma frase maior: ")
palavra1 = input("digite uma palavra: ")
print()
while len(palavra1) < 3:
    palavra1 = input("digite uma palvra maior ou igual 3 caracteres: ")
print("VERIFICAÇAO DA PRIMEIRA PALAVRA DIGITADA")
print()
cont = 0
for i in frase:
    if i  == palavra1:
        print("A palavra '{}' aparece na frase no indice {}".format(i,cont))
    cont +=1
print()
palavra2 = input("digite uma palavra: ")
print()
print("VERIFICAÇAO DA SEGUNDA PALAVRA DIGITADA")
print()
while len(palavra2) < 3:
    palavra2 = input("digite uma palavra com 3 ou mais caracteres: ") 
cont2 = 0
for i in frase:
    if i == palavra2:
        print("A palavra '{}' aparece na frase, no indice {}".format(i,cont2))
    cont2 +=1