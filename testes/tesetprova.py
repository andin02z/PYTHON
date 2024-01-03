
class extintor:
   peça_mangueira = False
   peça_cilindro = False
   peça_gatilho = False
   acionado = False

   def acionar(self):
    self.acionado = True
    print('extintor acionado')

    def desativar(self):
        self.acionado = False
        self.peça_mangueira = False
        self.peça_cilindro = False
        self.peça_gatilho = False
        print('extintor desativado')

        def pegar_extintor(self):
            if self.desativado == True:
                self.peça_cilindro = True

        def pegar_cilindro(self):
            if self.acionado == True:
                if self.peça_mangueira == False:
                    self. peça_mangueira = True

        def peça_mangueira(self):
            if self.acionado == True and self.peça_mangueira == True and self.peça_cilindro == True:
                self.peça_gatilho = True
            else:
                print('observe as peças') 


        def validar_acionado(self):
            if self.acionado == True:
                return ' acionado'
            else:
                return 'desativado'        

        def validar_gatilho(self):
            if self.peça_gatilho == True:
                return 'OK'
            else:
                return 'verifique...'
            if self.acionado == True:
                return 'acionado'
            else:
                return 'desativado'

        def validar_mamgueira(self):
            if self.peça_mangueira == True:
                return ' com a mangueira'
            else:
                return 'sem a mangueira'

        def validar_cilindro(self):
            if self.peça_cilindro == True:
                return 'cilindro cheio'
            else:
                return 'cilindro vazio'
            


        def __str__(self):
            return f'o extintor está { self.validar_acionado() }, a peça cilindro está { self.validar_cilindro ()}, a peça mangueira está { self.validar_mamgueira()},e a peça gatilho está { self.validar_gatilho()},'         
            
    
          
    def __str__(self):
        return f'A cafeteira está { self.valida_ligada() }, o compartimento de agua está { self.valida_agua() }, o compartimento do filtro está { self.valida_filtro() }. E o café: { self.valida_cafe() },'
    
pegar_extintor = extintor()

#print(pegar_extintor)

#pegar_extintor.acionar()

#print(pegar_extintor)

#pegar_extintor.pegar_mangueira()

#print(pegar_extintor)

#pegar_extintor.acionar_gatilho()

print(extintor)

