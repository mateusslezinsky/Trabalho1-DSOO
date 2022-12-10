import PySimpleGUI as sg
from limite.tela_abstrata import TelaAbstrata
from operator import itemgetter


class TelaChapa(TelaAbstrata):
    def __init__(self, controlador_chapa):
        self.__controlador_chapa = controlador_chapa

    def tela_chapa_opcoes(self):
        return self.__controlador_chapa.controlador_sistema.tela_sistema.menu_base("Chapas")

    def cadastrar_chapa(self):
        layout = [
            [self.text('Cadastro de chapa', fontSize=25)],
            [self.text('Nome da chapa:'),
             self.input_text('', key='nome')],
            [self.text('ID da chapa:      '),
             self.slider(key='id')],
            [self.confirm_button(), self.cancel_button('Voltar')]
        ]
        self.window = sg.Window(
            'Cadastro de chapas').Layout(layout)
        button, values = self.window.Read()
        if button == "Voltar":
            self.window.Close()
            return None
        else:
            nome = values["nome"].title().strip()
            id = values["id"]
            self.window.Close()
            return {"nome": nome, "id": id}

    def error(self, error):
        self.window = sg.Popup(error, title="Erro", font=("Helvetica", 18))

    def mostra_chapa(self, dados):
        if dados is not None:
            dados_consultados = f"Nome cadastrado atualmente para a chapa: {dados.nome} \nID cadastrado atualmente para a chapa: {dados.id}"
            self.window = sg.Popup(
                dados_consultados, title="Dados da chapa consultada", font=("Helvetica", 18))

        else:
            self.error("Não foi possível encontrar a chapa desejada!")

    def alterar_chapa(self, chapa):
        layout = [
            [self.text('Alteração de chapa', fontSize=25)],
            [self.text('Nome da chapa:'),
             self.input_text(chapa.nome, key='nome')],
            [self.text('ID da chapa:      '),
             self.slider(value=chapa.id, key='id')],
            [self.confirm_button(), self.cancel_button('Voltar')]
        ]
        self.window = sg.Window(
            'Alteração de chapa').Layout(layout)
        button, values = self.window.Read()
        if button == "Voltar":
            self.window.Close()
            return None
        else:
            nome = values["nome"].title().strip()
            id = values["id"]
            self.window.Close()
            return {"nome": nome, "id": id}

    def consultar_chapa(self):
        layout = [
            [self.text('Consulta de chapa', fontSize=25)],
            [self.text('ID da chapa:      '),
             self.slider(key='id')],
            [self.confirm_button(), self.cancel_button('Voltar')]
        ]
        self.window = sg.Window(
            'Consulta de chapas').Layout(layout)
        button, values = self.window.Read()
        if button == "Voltar":
            self.window.Close()
            return None
        else:
            id = values["id"]
            self.window.Close()
            return id

    def exclui_chapa(self, dados):
        dados_consultados = f"Essa chapa foi excluída:\n\nNome cadastrado para a chapa: {dados.nome} \nID cadastrado para a chapa: {dados.id}"
        self.window = sg.Popup(
            dados_consultados, title="Exclusão de chapa", font=("Helvetica", 18))

    def mostrar_todos(self):
        dados_consultados = ""
        total = 0
        for index, chapa in enumerate(sorted(self.__controlador_chapa.chapas.get_all())):
            dados_consultados += f"\n{index+1} - Chapa de nome: {chapa.nome}\n ID: {chapa.id}\n"
            total += 1
        self.window = sg.Popup(
            dados_consultados + f"\nO total cadastrado é: {total}", title="Consulta de todas as chapas", font=("Helvetica", 18))
