import PySimpleGUI as sg


class TelaSistema:
    def __init__(self, controlador_sistema):
        self.opcao_crud = 0
        self.__controlador_sistema = controlador_sistema
        self.__window = None
        self.init_components()

    def tela_principal(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_components(self):
        sg.ChangeLookAndFeel("DarkTeal4")
        layout = [
            [sg.Text("Eleições Reitoria", font=("Helvetica", 25))],
            [sg.Radio("Chapas", "RD2", key="1")],
            [sg.Radio("Candidatos", "RD1", key="2")],
            [sg.Radio("Eleitores", "RD1", key="3")],
            [sg.Radio("Funções da urna", "RD1", key="4")],
            [sg.Radio("Sair", "RD1", key="0")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]
        self.__window = sg.Window("Eleições Reitoria").Layout(layout)

    def close(self):
        self.__window.Close()

    def menu_base(self, menu):
        print("\n")
        print("{} {} {}".format("-"*10, menu, "-"*10))
        print("1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Consultar")
        print("4 - Excluir")
        print("0 - Voltar")
        opcao = int(input("\nEscolha sua opção: "))
        if menu == "Candidatos":
            self.__controlador_sistema.controlador_candidatos.opcao_crud = opcao
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

    def mensagem_redefine_sistema(self):
        print("O sistema e a urna foram redefinidos")
