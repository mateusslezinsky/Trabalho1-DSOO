from entidade.eleitor import TipoEleitor
from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaEleitor(TelaAbstrata):
    def __init__(self, controlador_eleitores):
        super().__init__()
        self.__controlador_eleitores = controlador_eleitores

    def tela_eleitor_opcoes(self):
        return self.__controlador_eleitores.controlador_sistema.tela_sistema.menu_base("Eleitores")

    def cadastra_eleitor(self):
        layout = [
            [self.text('Cadastro de eleitor', fontSize=25)],
            [self.text('Nome:'),
             self.input_text('', key='nome')],
            [self.text('CPF:  '),
             self.input_text('', key='cpf')],
            [self.text('Tipo de eleitor:')],
            [self.input_radio('Aluno', key=str(
                TipoEleitor.ALUNO.value), default=True)],
            [self.input_radio('Professor', key=str(
                TipoEleitor.PROFESSOR.value))],
            [self.input_radio('Servidor', key=str(
                TipoEleitor.SERVIDOR.value))],
            [self.confirm_button(), self.cancel_button('Voltar')]
        ]
        self.window = sg.Window(
            'Cadastro de eleitor').Layout(layout)
        button, values = self.window.Read()
        if button in (None, 'Voltar'):
            self.window.Close()
            return None
        else:
            nome = values["nome"].title().strip()
            cpf = values["cpf"]
            dados_basicos = {"nome": nome, "cpf": cpf}
            if values[str(TipoEleitor.ALUNO.value)]:
                dados_basicos["tipo_eleitor"] = TipoEleitor.ALUNO.value
            elif values[str(TipoEleitor.PROFESSOR.value)]:
                dados_basicos["tipo_eleitor"] = TipoEleitor.PROFESSOR.value
            elif values[str(TipoEleitor.SERVIDOR.value)]:
                dados_basicos["tipo_eleitor"] = TipoEleitor.SERVIDOR.value
            self.window.Close()
        return dados_basicos

    def mostra_eleitor(self, eleitor, extra=''):
        if eleitor is not None:
            dados_consultados = f"Nome cadastrado atualmente para o eleitor: {eleitor.nome} \nCPF cadastrado atualmente para o eleitor: {eleitor.cpf}\n"
            tipo_eleitor = ""
            if eleitor.tipo_eleitor == TipoEleitor.ALUNO.value:
                tipo_eleitor = "\nO tipo de eleitor é: Aluno\n"
            elif eleitor.tipo_eleitor == TipoEleitor.PROFESSOR.value:
                tipo_eleitor = "\nO tipo de eleitor é: Professor\n"
            elif eleitor.tipo_eleitor == TipoEleitor.SERVIDOR.value:
                tipo_eleitor = "\nO tipo de eleitor é: Servidor\n"

            self.window = sg.Popup(
                extra + dados_consultados + tipo_eleitor, title="Dados do eleitor",
                font=("Helvetica", 18))
        else:
            self.error("Não foi possível encontrar o eleitor desejado!")

    def consulta_eleitor(self):
        layout = [
            [self.text('Consulta de eleitor', fontSize=25)],
            [self.text('CPF:      '),
             self.input_text('', key='cpf')],
            [self.confirm_button(), self.cancel_button('Voltar')]
        ]
        self.window = sg.Window(
            'Consulta de eleitor').Layout(layout)
        button, values = self.window.Read()
        if button in (None, 'Voltar'):
            self.window.Close()
            return None
        else:
            cpf = values["cpf"]
            self.window.Close()
            return cpf

    def altera_eleitor(self, eleitor):
        layout = [
            [self.text('Alteração de eleitor', fontSize=25)],
            [self.text('Nome:'),
             self.input_text(eleitor.nome, key='nome')],
            [self.text('CPF:  '),
             self.input_text(eleitor.cpf, key='cpf')],
            [self.input_radio('Aluno', key=str(TipoEleitor.ALUNO.value), default=(
                True if eleitor.tipo_eleitor == TipoEleitor.ALUNO.value else False))],
            [self.input_radio('Professor', key=str(TipoEleitor.PROFESSOR.value), default=(
                True if eleitor.tipo_eleitor == TipoEleitor.PROFESSOR.value else False))],
            [self.input_radio('Servidor', key=str(TipoEleitor.SERVIDOR.value), default=(
                True if eleitor.tipo_eleitor == TipoEleitor.SERVIDOR.value else False))],
            [self.confirm_button(), self.cancel_button('Voltar')]
        ]
        self.window = sg.Window('Alteração de eleitor').Layout(layout)
        button, values = self.window.Read()
        if button in (None, 'Voltar'):
            self.window.Close()
            return None
        else:
            nome = values["nome"].title().strip()
            cpf = values["cpf"]
            dados_basicos = {"nome": nome, "cpf": cpf}
            if values[str(TipoEleitor.ALUNO.value)]:
                dados_basicos["tipo_eleitor"] = TipoEleitor.ALUNO.value
            elif values[str(TipoEleitor.PROFESSOR.value)]:
                dados_basicos["tipo_eleitor"] = TipoEleitor.PROFESSOR.value
            elif values[str(TipoEleitor.SERVIDOR.value)]:
                dados_basicos["tipo_eleitor"] = TipoEleitor.SERVIDOR.value
        self.window.Close()
        return dados_basicos

    def exclui_eleitor(self, eleitor):
        self.mostra_eleitor(
            eleitor, extra="O eleitor abaixo foi excluído:\n\n")

    def error(self, error):
        self.window = sg.Popup(error, title="Erro", font=("Helvetica", 18))

    def mostrar_todos(self):
        dados_consultados = ""
        divider = "-"*50
        total = 0
        for index, eleitor in enumerate(sorted(self.__controlador_eleitores.eleitores.get_all())):
            if eleitor.tipo_eleitor == TipoEleitor.ALUNO.value:
                dados_consultados += f"\n{index+1} - Eleitor de nome: {eleitor.nome}\n CPF: {eleitor.cpf}\n Tipo do eleitor: Aluno\n{divider}"
            elif eleitor.tipo_eleitor == TipoEleitor.PROFESSOR.value:
                dados_consultados += f"\n{index+1} - Eleitor de nome: {eleitor.nome}\n CPF: {eleitor.cpf}\n Tipo do eleitor: Professor\n{divider}"
            elif eleitor.tipo_eleitor == TipoEleitor.SERVIDOR.value:
                dados_consultados += f"\n{index+1} - Eleitor de nome: {eleitor.nome}\n CPF: {eleitor.cpf}\n Tipo do eleitor: Servidor\n{divider}"

            total = index + 1
        self.window = sg.Popup(
            dados_consultados + f"\nO total cadastrado é: {total}", title="Consulta de todas os eleitores", font=("Helvetica", 18))
