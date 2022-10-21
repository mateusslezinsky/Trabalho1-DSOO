class TelaSistema:
    def __init__(self, controlador_sistema):
        self.opcao_crud = 0
        self.__controlador_sistema = controlador_sistema

    def tela_principal(self):
        print("\n")
        print("-"*10, " Eleições Reitoria ", "-"*10)
        print("1 - Chapas")
        print("2 - Candidatos")
        print("3 - Eleitores")
        print("4 - Homologação de Urna")
        print("5 - Início de Votação")
        print("6 - Resultados")
        print("0 - Sair")
        opcao = int(input("\nEscolha sua opção: "))
        return opcao

    def menu_base(self, menu):
        print("\n")
        print("{} {} {}".format("-"*10, menu, "-"*10))
        print("1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Consultar")
        print("4 - Excluir")
        print("0 - Voltar")
        opcao = int(input("\nEscolha sua opção: "))
        self.__controlador_sistema.controlador_candidato.opcao_crud = opcao
        return opcao

    def lida_com_erro(self):
        print("\nDigite uma opção válida!")

    def verifica_int(self, mensagem):
        while True:
            try:
                variavel = int(input(mensagem))
                break
            except ValueError:
                print("\nO valor digitado não é válido. Tente novamente!")
        return variavel
