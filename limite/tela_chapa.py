class TelaChapa:
    def tela_chapa_opcoes(self):
        print("\n")
        print("{} Chapas {}".format("-"*10, "-"*10))
        print("\n1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Consultar")
        print("4 - Excluir")
        print("0 - Voltar")
        opcao = int(input("\nEscolha sua opção: "))
        return opcao
