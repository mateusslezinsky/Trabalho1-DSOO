class TelaCandidato:
    def __init__(self, controlador_candidato):
        self.__controlador_candidato = controlador_candidato

    def tela_candidato_opcoes(self):
        return self.__controlador_candidato.controlador_sistema.tela_sistema.menu_base("Candidatos")

    def tela_escolha_cadastro(self):
        print("\n")
        if self.__controlador_candidato.opcao_crud == 1:
            print("-"*10, "Cadastro", "-"*10)
        if self.__controlador_candidato.opcao_crud == 2:
            print("-"*10, "Alteração", "-"*10)
        if self.__controlador_candidato.opcao_crud == 3:
            print("-"*10, "Consulta", "-"*10)
        if self.__controlador_candidato.opcao_crud == 4:
            print("-"*10, "Exclusão", "-"*10)
        print("1 - Reitor")
        print("2 - Pró-Reitor")
        print("0 - Voltar")
        opcao = int(input("\nEscolha sua opção: "))
        return opcao
