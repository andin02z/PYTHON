# CRUD - created, readed, updated e deleted


dic = {'nome': 'paulo'} # created
dic2 = dict(idade=22) 

dic['nome'] #readed
reading = dic2.get('idade') # readed  

dic.update(sobrenome='junior') #update ou inserindo dados
dic.update({'idade':23})
tupla = ('peso', 72.12),
lista = ['data','13/04/1996']
dic.update(lista),
dic.update(tupla)

print(dic)
print(dic2) 

dic.clear()# lipar dicionario 