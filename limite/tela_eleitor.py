from entidade.eleitor import TipoEleitor
import PySimpleGUI as sg



class TelaEleitor:
    def __init__(self, controlador_eleitores):
        self.__controlador_eleitores = controlador_eleitores
        self.__window = None
        self.init_components()

    def tela_eleitor_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_components(self):
        sg.ChangeLookAndFeel("DarkTeal4")
        layout = [
            [sg.Text("Eleitores", font=("Helvetica", 25))],
            [sg.Radio("Cadastrar", "RD2", key="1")],
            [sg.Radio("Alterar", "RD1", key="2")],
            [sg.Radio("Consultar", "RD1", key="3")],
            [sg.Radio("Excluir", "RD1", key="4")],
            [sg.Radio("Voltar", "RD1", key="0")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]
        self.__window = sg.Window("Eleições Reitoria").Layout(layout)

    def close(self):
        self.__window.Close()

    def cadastra_eleitor(self):
        nome = input("\nDigite o nome do eleitor: ").title().strip()
        while len(nome) == 0:
            nome = input("Inválido! Insira o nome novamente: ").title()
        cpf = self.__controlador_eleitores.controlador_sistema.tela_sistema.verifica_int(
            "Digite o CPF do eleitor: ")
        while self.__controlador_eleitores.checa_se_ja_existe(cpf, self.__controlador_eleitores.eleitores):
            cpf = self.__controlador_eleitores.controlador_sistema.tela_sistema.verifica_int(
                "Já existe! Digite outro CPF para o eleitor: ")

        print("\nEscolha um tipo de eleitor, sendo:")
        print("1 - Aluno")
        print("2 - Professor")
        print("3 - Servidor")
        tipo_eleitor = self.__controlador_eleitores.controlador_sistema.tela_sistema.verifica_int(
            "Escolha a sua opção: ")

        def verifica_tipo():
            for tipo in TipoEleitor:
                if tipo.value == tipo_eleitor:
                    return True
            else:
                return False

        while True:
            resultado = verifica_tipo()
            if resultado:
                break
            else:
                tipo_eleitor = self.__controlador_eleitores.controlador_sistema.tela_sistema.verifica_int(
                    "Inválido! Escolha a sua opção novamente: ")

        return {"nome": nome, "cpf": cpf, "tipo_eleitor": tipo_eleitor}

    def mostra_eleitor(self, dados):
        if dados is None:
            print("Não foi possível encontrar o eleitor!")
        else:
            print("\nEleitor cadastrado:")
            print("Nome:", dados.nome)
            print("CPF:", dados.cpf)
            if dados.tipo_eleitor == 1:
                print("Tipo de eleitor: aluno")
            elif dados.tipo_eleitor == 2:
                print("Tipo de eleitor: professor")
            elif dados.tipo_eleitor == 3:
                print("Tipo de eleitor: servidor")

    def consulta_eleitor(self):
        cpf = self.__controlador_eleitores.controlador_sistema.tela_sistema.verifica_int(
            "Digite o CPF do eleitor: ")
        return cpf

    def exclui_eleitor(self):
        print("O eleitor acima foi excluído com sucesso!")
