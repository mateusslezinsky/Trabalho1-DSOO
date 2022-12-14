import PySimpleGUI as sg
from limite.tela_abstrata import TelaAbstrata


class TelaSistema(TelaAbstrata):
    def __init__(self, controlador_sistema):
        super().__init__()
        self.opcao_crud = 0
        self.__controlador_sistema = controlador_sistema

    def tela_principal(self):
        self.init_components({
            "title": "Eleições Reitoria",
            "key1": "Chapas",
            "key2": "Candidatos",
            "key3": "Eleitores",
            "key4": "Funções da Urna",
            "key5": "",
            "key0": "Sair",
        })
        button, values = self.window.Read()
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

    def close(self):
        self.window.Close()

    def menu_base(self, menu):
        self.init_components({
            "title": menu,
            "key1": "Cadastrar",
            "key2": "Alterar",
            "key3": "Consultar",
            "key4": "Excluir",
            "key5": "Mostrar cadastros",
            "key0": "Voltar"
        })
        button, values = self.window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['5']:
            opcao = 5
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        if menu == "Candidatos":
            self.__controlador_sistema.controlador_candidatos.opcao_crud = opcao
        self.close()
        return opcao

    def lida_com_erro(self):
        sg.Popup("Digite uma opção válida!",
                 title="Erro", font=("Helvetica", 18))

    def mensagem_redefine_sistema(self):
        self.window = sg.Popup(
            "A urna foi redefinida", title="Mensagem", font=("Helvetica", 18))
