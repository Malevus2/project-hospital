class paciente:
    dic={}

    def __init__(self,nome,idade,crm,numero): #caracteristicas do usuario.
        self.__nome = nome
        self.idade = idade
        self.crm = crm
        self.numero = numero

        #Getter
    @property
    def nome_aluno(self):
        return self.__nome
    
    #Setter
    @nome_aluno.setter
    def nome_aluno(self, novo_nome):
        self.__nome = novo_nome

    def Cadastrarpaciente(self):
        self.dic[self.__nome] = {"nome":self.__nome}, {"idade": self.idade}, {"crachá": self.crm}, {"Contato": self.numero}

    def Listarpaciente(self,nome):
        try:
            nomeEncontradopaciente = self.dic[nome]
        except (KeyError):
            print("nome não existente.")
        else:
            return nomeEncontradopaciente