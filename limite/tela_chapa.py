class TelaChapa:
    def __init__(self, controlador_chapa):
        self.__controlador_chapa = controlador_chapa

    def tela_chapa_opcoes(self):
        return self.__controlador_chapa.controlador_sistema.tela_sistema.menu_base("Chapas")

    def tratamento_id(self, lista, tipo):
        while True:
            try:
                id = int(
                    input("Digite um número de identificação da chapa (ID): "))
                if tipo == "Cadastro":
                    for chapa in lista:
                        if id == chapa.id:
                            print("ID já cadastrado!")
                            break
                    else:
                        break
                elif tipo == "Consulta":
                    break

            except ValueError:
                print("\nO valor digitado não é válido. Tente novamente!")
        return id

    def cadastrar_chapa(self, lista):
        nome = input("\nInsira aqui o nome da chapa: ").title().strip()
        while len(nome) == 0:
            nome = input("Inválido! Insira o nome novamente: ").title()

        id = self.tratamento_id(lista, "Cadastro")
        return {"nome": nome, "id": id}

    def mostra_chapa(self, dados):
        if dados is None:
            print("Não foi possível encontrar a chapa desejada!")
        else:
            print("\nNome cadastrado atualmente para a chapa: ", dados.nome)
            print("ID cadastrado atualmente para a chapa: ", dados.id)

    def consultar_chapa(self, lista):
        id = self.tratamento_id(lista, "Consulta")
        return id

    def exclui_chapa(self):
        print("A chapa acima foi excluída com sucesso!")
