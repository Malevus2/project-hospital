import paciente as c
import medico as b
import acompanhante as a
while True:
    print(" Seja bem-vindo ao The best hospital o brazil!!")
    print("1- cadastrar paciente")
    print("2- cadastrar medico")
    print("3- cadastrar acompanhante")
    print("4- buscar paciente")
    print("5- buscar medico")
    print("6- buscar acompanhante")
    print("7- Sair")
    opcao = int(input("Digite a opção que deseja: "))
    if opcao == 1:
        nome = input("nome: ")
        idade = int(input(" Digite sua idade: "))
        crm = input("Qual o crm do paciente: ")
        numero = int(input("numero do paciente: "))
        user01= c.paciente(nome,idade,crm,numero)
        user01.Cadastrarpaciente()
        print("Paciente cadastrado com sucesso!")

    elif opcao == 2:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        crm = int(input(" Digite sua crm: "))
        numero = int(input("Digite o telefone para contato: "))
        user02 = b.medico(nome,idade,crm,numero)
        user02.CadastrarMedico()
        print("Médico cadastrado com sucesso!")
    
    elif opcao == 3:
        nome = input("nome: ")
        idade = int(input(" Digite sua idade: "))
        numero = int(input("numero do acompanhante: "))
        user03= a.acompanhante(nome,idade,numero)
        user03.CadastrarAcompanhante()
        print("Paciente cadastrado com sucesso!")

    elif opcao == 4:
        nomeBuscado = input("Qual nome você deseja : ")
        dadosEncontradospaciente = user01.Listarpaciente(nomeBuscado)
        print(dadosEncontradospaciente)

    elif opcao == 5:
        nomeBuscado = input("Qual nome você deseja buscar: ")
        dadosEncontradosMedico = user02.ListarMedico(nomeBuscado)
        print(dadosEncontradosMedico)
        print("Médico encontrado com sucesso!!")
    elif opcao == 6:
        nomeBuscado = input("Qual o nome do acompanhante que deseja ser buscado: ")
        dadosEncontradosAcompanhante = user03.ListarAcompanhante(nomeBuscado)
        print(dadosEncontradosAcompanhante)

    elif opcao == 7:
        print(" Até a próxima!")
        break