class TelaSistema:
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
        print("\n1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Consultar")
        print("4 - Excluir")
        print("0 - Voltar")
        opcao = int(input("\nEscolha sua opção: "))
        return opcao
