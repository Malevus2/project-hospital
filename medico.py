class medico:
    dic={}

    def __init__(self,nome,idade,crm,numero): #caracteristicas do usuario.
        self.__nome = nome
        self.idade = idade
        self.crm = crm
        self.numero = numero

        #Getter
    @property
    def nome_medico(self):
        return self.__nome
    
    #Setter
    @nome_medico.setter
    def nome_medico(self, novo_nome):
        self.__nome = novo_nome

    def CadastrarMedico(self):
        self.dic[self.__nome] = {"nome":self.__nome}, {"idade": self.idade}, {"crachá": self.crm}, {"Contato": self.numero}

    def ListarMedico(self,nome):
        try:
            nomeEncontradomedico = self.dic[nome]
        except (KeyError):
            print("nome não existente.")
        else:
            return nomeEncontradomedico
        # importar de um file e nomeiar de c