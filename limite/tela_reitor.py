class TelaReitor:
    def __init__(self, controlador_reitores):
        self.__controlador_reitores = controlador_reitores

    def cadastrar_reitor(self):
        nome = input("Digite o nome do reitor: ").title().strip()
        while len(nome) == 0:
            nome = input("Inválido! Insira o nome novamente: ").title()
        numero = self.__controlador_reitores.controlador_candidatos.controlador_sistema.tela_sistema.verifica_int(
            "Digite o número do reitor: ")

        while self.__controlador_reitores.checa_se_ja_existe(numero):
            numero = self.__controlador_reitores.controlador_candidatos.controlador_sistema.tela_sistema.verifica_int(
                "Já existe! Digite um outro número pro reitor: ")

        return {"nome": nome, "numero": numero}

    def consulta_reitor(self):
        numero = self.__controlador_reitores.controlador_candidatos.controlador_sistema.tela_sistema.verifica_int(
            "Digite o número do reitor: ")
        return numero

    def imprime_dados(self, reitor):
        if reitor is None:
            print("Não foi possível encontrar o reitor!")
        elif reitor is not None:
            print("\nNome cadastrado atualmente para o reitor: ", reitor.nome)
            print("Número cadastrado atualmente para o reitor: ", reitor.numero)
            print("\n")
            print("-" * 10, "Chapa", "-" * 10)
            print("\nNome da chapa cadastrada atualmente para o reitor: ",
                  reitor.chapa.nome)
            print("ID da chapa cadastrada atualmente para o reitor: ", reitor.chapa.id)

    def remove_reitor(self):
        print("\nO reitor acima foi excluído com sucesso!")
