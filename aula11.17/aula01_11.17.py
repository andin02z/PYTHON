# while condição:
#    codigo 
#    impplementar o contador 
# break = quebra as estruturas de repetição 
# for contador:
#  codigo
# peça a idade de 20 alunos. faça um codigo que avisa quando o aluno tem mais de 13 anos.

contador = 0 
while contador < 20 :
    idade_aluno = int(input ('informe sua idade: '))
    if idade_aluno > 13: 
        print(f'o aluno{ contador } tem mais de 13 anos ')