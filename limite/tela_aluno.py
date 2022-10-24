class TelaAluno:
    def __init__(self, controlador_aluno):
        self.__controlador_aluno = controlador_aluno

    def tela_aluno_opcoes(self):
        return self.__controlador_aluno.controlador_sistema.tela_sistema.menu_base("Alunos")

    def tratamento_cpf(self, lista, tipo):
        while True:
            try:
                cpf = int(
                    input("Digite o CPF do aluno: "))
                if tipo == "Cadastro":
                    for aluno in lista:
                        if cpf == aluno.cpf:
                            print("CPF já cadastrado!")
                            break
                    else:
                        break
                elif tipo == "Consulta":
                    break

            except ValueError:
                print("\nO valor digitado não é válido. Tente novamente!")
        return cpf

    def tratamento_matricula(self, lista, tipo):
        while True:
            try:
                matricula = int(input("Digite a matrícula do aluno: "))
                if tipo == "Cadastro":
                    for aluno in lista:
                        if matricula == aluno.matricula:
                            print("Matrícula já cadastrada!")
                            break
                    else:
                        break
                elif tipo == "Consulta":
                    break

            except ValueError:
                print("\nO valor digitado não é válido. Tente novamente!")
        return matricula

    def cadastra_aluno(self, lista):
        nome = input("\nInsira aqui o nome do aluno: ").title().strip()
        while len(nome) == 0:
            nome = input("Inválido! Insira o nome novamente: ").title()

        cpf = self.tratamento_cpf(lista, "Cadastro")
        matricula = self.tratamento_matricula(lista, "Cadastro")
        return {"nome": nome, "cpf": cpf, "matricula": matricula}

    @staticmethod
    def imprime_dados(dados):
        if dados is None:
            print("Não foi possível encontrar o aluno desejado!")
        else:
            print("\nNome cadastrado atualmente para o aluno: ", dados.nome)
            print("CPF cadastrado atualmente para o aluno: ", dados.cpf)
            print("Matrícula cadastrada atualmente para o aluno: ", dados.matricula)

    def consulta_aluno(self, lista):
        cpf = self.__controlador_aluno.controlador_sistema.tela_sistema.verifica_int(
            "Digite o CPF do aluno: ")
        return cpf

    def exclui_aluno(self):
        print("O aluno acima foi excluído com sucesso!")
