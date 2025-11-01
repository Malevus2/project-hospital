class acompanhante:
    dic = {}

    def __init__(self,nome,idade,numero): #caracteristicas do usuario.
        self.__nome = nome
        self.idade = idade
        self.numero = numero

        #Getter
    @property
    def nome_aluno(self):
        return self.__nome
    
    #Setter
    @nome_aluno.setter
    def nome_acompanhante(self, novo_nome):
        self.__nome = novo_nome

    def CadastrarAcompanhante(self):
        self.dic[self.__nome] = {"nome":self.__nome}, {"idade": self.idade}, {"Contato": self.numero}

    def ListarAcompanhante(self,nome):
        try:
            nomeEncontradoAcompanhante = self.dic[nome]
        except (KeyError):
            print("nome não existente.")
        else:
            return nomeEncontradoAcompanhante


