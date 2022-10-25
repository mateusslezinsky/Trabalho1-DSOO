class TelaEleitor:
    def __init__(self, controlador_eleitores):
        self.__controlador_eleitores = controlador_eleitores

    def tela_eleitor_opcoes(self):
        return self.__controlador_eleitores.controlador_sistema.tela_sistema.menu_base("Eleitores")

    def cadastra_eleitor(self, lista):
        nome = input("Digite o nome do candidato: ").title().strip()
        while len(nome) == 0:
            nome = input("Inválido! Insira o nome novamente: ").title()
        cpf = self.__controlador_eleitores.controlador_sistema.tela_sistema.verifica_int(
            "Digite o CPF do eleitor: ")
        return {"nome": nome, "cpf": cpf}

    def mostra_eleitor(self, dados):
        if dados is None:
            print("Não foi possível encontrar o eleitor!")
        else:
            print("\nEleitor cadastrado:")
            print("Nome: ", dados.nome)
            print("CPF: ", dados.cpf)


    def consulta_eleitor(self, lista):
        cpf = self.__controlador_eleitores.controlador_sistema.tela_sistema.verifica_int(
            "Digite o CPF do eleitor: ")
        return cpf

    def exclui_eleitor(self):
        print("O eleitor acima foi excluído com sucesso!")