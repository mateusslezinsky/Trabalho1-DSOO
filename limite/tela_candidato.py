from entidade.pro_reitor import ProReitor, TipoProReitor


class TelaCandidato:
    def _init_(self, controlador_candidatos):
        self.__controlador_candidatos = controlador_candidatos

    def tela_candidato_opcoes(self):
        return self.__controlador_candidatos.controlador_sistema.tela_sistema.menu_base("Candidatos")

    def tela_escolha_cadastro(self):
        print("\n")
        if self.__controlador_candidatos.opcao_crud == 1:
            print("-"*10, "Cadastro", "-"*10)
        if self.__controlador_candidatos.opcao_crud == 2:
            print("-"*10, "Alteração", "-"*10)
        if self.__controlador_candidatos.opcao_crud == 3:
            print("-"*10, "Consulta", "-"*10)
        if self.__controlador_candidatos.opcao_crud == 4:
            print("-"*10, "Exclusão", "-"*10)
        print("1 - Reitor")
        print("2 - Pró-Reitor")
        print("0 - Voltar")
        opcao = int(input("\nEscolha sua opção: "))
        return opcao

    def cadastrar_candidato(self):
        nome = input("Digite o nome do candidato: ").title().strip()
        while len(nome) == 0:
            nome = input("Inválido! Insira o nome novamente: ").title()
        numero = self.__controlador_candidatos.controlador_sistema.tela_sistema.verifica_int(
            "Digite o número do candidato (1-98): ")
        while not 1 <= numero <= 98:
            numero = self.__controlador_candidatos.controlador_sistema.tela_sistema.verifica_int(
                "Digite um número válido para o candidato: ")

        while self._controlador_candidatos.checa_se_ja_existe(numero, self._controlador_candidatos.candidatos):
            numero = self.__controlador_candidatos.controlador_sistema.tela_sistema.verifica_int(
                "Já existe! Digite um outro número pro candidato: ")

            while not 1 <= numero <= 98:
                numero = self.__controlador_candidatos.controlador_sistema.tela_sistema.verifica_int(
                    "Digite um número válido para o candidato: ")

        dados_basicos = {"nome": nome, "numero": numero}

        if self.__controlador_candidatos.opcao_tipo_candidato == 2:
            print("\nEscolha um tipo de pró reitor, sendo:")
            print("1 - Graduação")
            print("2 - Extensão")
            print("3 - Pesquisa")
            tipo_pro_reitor = self.__controlador_candidatos.controlador_sistema.tela_sistema.verifica_int(
                "\nEscolha a sua opção: ")

            def verifica_tipo():
                for tipo in TipoProReitor:
                    if tipo.value == tipo_pro_reitor:
                        return True
                else:
                    return False

            while True:
                resultado = verifica_tipo()
                if resultado:
                    break
                else:
                    tipo_pro_reitor = self.__controlador_candidatos.controlador_sistema.tela_sistema.verifica_int(
                        "Inválido! Escolha a sua opção novamente: ")

            dados_basicos["tipo_pro_reitor"] = tipo_pro_reitor

        return dados_basicos

    def consulta_candidato(self):
        numero = self.__controlador_candidatos.controlador_sistema.tela_sistema.verifica_int(
            "Digite o número do candidato: ")
        return numero

    def imprime_dados(self, candidato):
        if candidato is None:
            print("Não foi possível encontrar o candidato!")
        elif candidato is not None:
            print("\nNome cadastrado atualmente para o candidato:", candidato.nome)
            print("Número cadastrado atualmente para o candidato:", candidato.numero)
            if isinstance(candidato, ProReitor):
                if candidato.tipo_pro_reitor == TipoProReitor.GRADUACAO.value:
                    print("O tipo de pró-reitor é: Graduação")
                elif candidato.tipo_pro_reitor == TipoProReitor.EXTENSAO.value:
                    print("O tipo de pró-reitor é: Extensão")
                elif candidato.tipo_pro_reitor == TipoProReitor.PESQUISA.value:
                    print("O tipo de pró-reitor é: Pesquisa")

            print("\n")
            print("-" * 10, "Chapa", "-" * 10)
            print("\nNome da chapa cadastrada atualmente para o candidato: ",
                  candidato.chapa.nome)
            print("ID da chapa cadastrada atualmente para o candidato: ",
                  candidato.chapa.id)

    def remove_candidato(self):
        print("\nO candidato acima foi excluído com sucesso!")
