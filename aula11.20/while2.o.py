# peça a idade de 20 alunos. faça um codigo que avisa quando o aluno tem mais de 13 anos
aluno = 1 
while aluno <= 20: 
    idade = int(input(f'qual a idade do aluno{ aluno}?'))
    if idade > 13: 
        print(f'a idade do aluno { aluno } é { idade } é maior que 13 ')