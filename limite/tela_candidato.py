from entidade.pro_reitor import ProReitor, TipoProReitor
from entidade.reitor import Reitor
from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaCandidato(TelaAbstrata):
    def __init__(self, controlador_candidatos):
        super().__init__()
        self.__controlador_candidatos = controlador_candidatos

    def tela_candidato_opcoes(self):
        return self.__controlador_candidatos.controlador_sistema.tela_sistema.menu_base("Candidatos")

    def tela_escolha_cadastro(self):
        layout = [
            [self.input_radio('Reitor', key="1")],
            [self.input_radio('Pró-Reitor', key="2")],
            [self.input_radio('Voltar', key="0")],
            [self.confirm_button(), self.cancel_button('Voltar')]
        ]
        if self.__controlador_candidatos.opcao_crud == 1:
            self.window = sg.Window(
                'Cadastro').Layout(layout)
        if self.__controlador_candidatos.opcao_crud == 2:
            self.window = sg.Window(
                'Alteração').Layout(layout)
        if self.__controlador_candidatos.opcao_crud == 3:
            self.window = sg.Window(
                'Consulta').Layout(layout)
        if self.__controlador_candidatos.opcao_crud == 4:
            self.window = sg.Window(
                'Exclusão').Layout(layout)
        button, values = self.window.Read()
        opcao = 0
        if values['0'] or button in (None, 'Voltar'):
            opcao = 0
        elif values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        self.window.Close()
        return opcao

    def cadastrar_candidato(self):
        if self.__controlador_candidatos.opcao_tipo_candidato == 1:
            layout = [
                [self.text('Cadastro de reitor', fontSize=25)],
                [self.text('Nome do reitor:'),
                 self.input_text('', key='nome')],
                [self.text('Número do reitor:      '),
                 self.slider(range=(1, 98), key='numero')],
                [self.confirm_button(), self.cancel_button('Voltar')]
            ]
        elif self.__controlador_candidatos.opcao_tipo_candidato == 2:
            layout = [
                [self.text('Cadastro de pró-reitor', fontSize=25)],
                [self.text('Nome do pró-reitor:'),
                 self.input_text('', key='nome')],
                [self.text('Número do pró-reitor:      '),
                 self.slider(range=(1, 98), key='numero')],
                [self.text('Tipo do pró-reitor:')],
                [self.input_radio('Graduação', default=True,
                                  key=str(TipoProReitor.GRADUACAO.value))],
                [self.input_radio('Extensão', key=str(
                    TipoProReitor.EXTENSAO.value))],
                [self.input_radio('Pesquisa', key=str(
                    TipoProReitor.PESQUISA.value))],
                [self.confirm_button(), self.cancel_button('Voltar')]
            ]
        self.window = sg.Window(
            'Cadastro de candidato').Layout(layout)
        button, values = self.window.Read()
        if button in (None, 'Voltar'):
            self.window.Close()
            return None
        else:
            nome = values["nome"].title().strip()
            numero = values["numero"]
            dados_basicos = {"nome": nome, "numero": numero}
            if self.__controlador_candidatos.opcao_tipo_candidato == 2:
                if values[str(TipoProReitor.GRADUACAO.value)]:
                    dados_basicos["tipo_pro_reitor"] = TipoProReitor.GRADUACAO.value
                elif values[str(TipoProReitor.EXTENSAO.value)]:
                    dados_basicos["tipo_pro_reitor"] = TipoProReitor.EXTENSAO.value
                elif values[str(TipoProReitor.PESQUISA.value)]:
                    dados_basicos["tipo_pro_reitor"] = TipoProReitor.PESQUISA.value
            self.window.Close()
            return dados_basicos

    def altera_candidato(self, candidato):
        if self.__controlador_candidatos.opcao_tipo_candidato == 1:
            layout = [
                [self.text('Alteração de reitor', fontSize=25)],
                [self.text('Nome do reitor:'),
                 self.input_text(candidato.nome, key='nome')],
                [self.text('Número do reitor:      '),
                 self.slider(value=candidato.numero, key='numero')],
                [self.confirm_button(), self.cancel_button('Voltar')]
            ]
        elif self.__controlador_candidatos.opcao_tipo_candidato == 2:
            layout = [
                [self.text('Alteração de pró-reitor', fontSize=25)],
                [self.text('Nome do pró-reitor:'),
                 self.input_text(candidato.nome, key='nome')],
                [self.text('Número do pró-reitor:      '),
                 self.slider(value=candidato.numero, key='numero')],
                [self.text('Tipo do pró-reitor:')],
                [self.input_radio('Graduação', default=(True if candidato.tipo_pro_reitor == TipoProReitor.GRADUACAO.value else False),
                                  key=str(TipoProReitor.GRADUACAO.value))],
                [self.input_radio('Extensão', default=(True if candidato.tipo_pro_reitor == TipoProReitor.EXTENSAO.value else False), key=str(
                    TipoProReitor.EXTENSAO.value))],
                [self.input_radio('Pesquisa', default=(True if candidato.tipo_pro_reitor == TipoProReitor.PESQUISA.value else False), key=str(
                    TipoProReitor.PESQUISA.value))],
                [self.confirm_button(), self.cancel_button('Voltar')]
            ]
        self.window = sg.Window(
            'Alteração de candidato').Layout(layout)
        button, values = self.window.Read()
        if button in (None, 'Voltar'):
            self.window.Close()
            return None
        else:
            nome = values["nome"].title().strip()
            numero = values["numero"]
            dados_basicos = {"nome": nome, "numero": numero}
            if self.__controlador_candidatos.opcao_tipo_candidato == 2:
                if values[str(TipoProReitor.GRADUACAO.value)]:
                    dados_basicos["tipo_pro_reitor"] = TipoProReitor.GRADUACAO.value
                elif values[str(TipoProReitor.EXTENSAO.value)]:
                    dados_basicos["tipo_pro_reitor"] = TipoProReitor.EXTENSAO.value
                elif values[str(TipoProReitor.PESQUISA.value)]:
                    dados_basicos["tipo_pro_reitor"] = TipoProReitor.PESQUISA.value
            self.window.Close()
            return dados_basicos

    def consulta_candidato(self):
        layout = [
            [self.text('Consulta de candidato', fontSize=25)],
            [self.text('Número do candidato:      '),
             self.slider(key='numero')],
            [self.confirm_button(), self.cancel_button('Voltar')]
        ]
        self.window = sg.Window(
            'Consulta de candidato').Layout(layout)
        button, values = self.window.Read()
        if button in (None, 'Voltar'):
            self.window.Close()
            return None
        else:
            numero = values["numero"]
            self.window.Close()
            return numero

    def imprime_dados(self, candidato, extra=""):
        if candidato is not None:
            dados_consultados = f"Nome cadastrado atualmente para o candidato: {candidato.nome} \nNúmero cadastrado atualmente para o candidato: {candidato.numero}\n"
            tipo_pro_reitor = ""
            if isinstance(candidato, ProReitor):
                if candidato.tipo_pro_reitor == TipoProReitor.GRADUACAO.value:
                    tipo_pro_reitor = "\nO tipo de pró-reitor é: Graduação\n"
                elif candidato.tipo_pro_reitor == TipoProReitor.EXTENSAO.value:
                    tipo_pro_reitor = "\nO tipo de pró-reitor é: Extensão\n"
                elif candidato.tipo_pro_reitor == TipoProReitor.PESQUISA.value:
                    tipo_pro_reitor = "\nO tipo de pró-reitor é: Pesquisa\n"

            chapa_consultada = f"\nNome da chapa cadastrada atualmente para o candidato: {candidato.chapa.nome} \nID da chapa cadastrada atualmente para o candidato: {candidato.chapa.id}"
            self.window = sg.Popup(
                extra + dados_consultados + tipo_pro_reitor + chapa_consultada, title="Dados do candidato", font=("Helvetica", 18))

        else:
            self.error("Não foi possível encontrar o candidato desejado!")

    def remove_candidato(self, candidato):
        self.imprime_dados(
            candidato, extra="O candidato abaixo foi excluído:\n\n")

    def imprime_resposta_segundo_turno(self):
        self.error(
            "O candidato não foi cadastrado/modificado. Motivo: segundo turno")

    def error(self, error):
        self.window = sg.Popup(error, title="Erro", font=("Helvetica", 18))

    def mostrar_todos(self):
        dados_consultados = ""
        divider = "-"*50
        total = 0
        for index, candidato in enumerate(sorted(self.__controlador_candidatos.candidatos.get_all())):
            if isinstance(candidato, Reitor):
                dados_consultados += f"\n{index+1} - Candidato de nome: {candidato.nome}\n Número: {candidato.numero}\n\n Chapa: {candidato.chapa.nome}\n ID de Chapa: {candidato.chapa.id}\n{divider}"
            elif isinstance(candidato, ProReitor):
                if candidato.tipo_pro_reitor == TipoProReitor.GRADUACAO.value:
                    dados_consultados += f"\n{index+1} - Candidato de nome: {candidato.nome}\n Número: {candidato.numero}\n Tipo do pró-reitor: Graduação \n\n Chapa: {candidato.chapa.nome}\n ID de Chapa: {candidato.chapa.id}\n{divider}"
                elif candidato.tipo_pro_reitor == TipoProReitor.EXTENSAO.value:
                    dados_consultados += f"\n{index+1} - Candidato de nome: {candidato.nome}\n Número: {candidato.numero}\n Tipo do pró-reitor: Extensão \n\n Chapa: {candidato.chapa.nome}\n ID de Chapa: {candidato.chapa.id}\n{divider}"
                elif candidato.tipo_pro_reitor == TipoProReitor.PESQUISA.value:
                    dados_consultados += f"\n{index+1} - Candidato de nome: {candidato.nome}\n Número: {candidato.numero}\n Tipo do pró-reitor: Pesquisa \n\n Chapa: {candidato.chapa.nome}\n ID de Chapa: {candidato.chapa.id}\n{divider}"

            total = index + 1
        self.window = sg.Popup(
            dados_consultados + f"\nO total cadastrado é: {total}", title="Consulta de todas os candidatos", font=("Helvetica", 18))
