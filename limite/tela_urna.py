from entidade.reitor import Reitor
from entidade.pro_reitor import ProReitor, TipoProReitor
from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaUrna(TelaAbstrata):
    def __init__(self, controlador_urna):
        super().__init__()
        self.__controlador_urna = controlador_urna

    def tela_principal(self):
        self.init_components({
            "title": "Urna",
            "key1": "Homologação de urna",
            "key2": "Votar",
            "key3": "Encerrar votação",
            "key4": "Resultados",
            "key5": "Definir turno",
            "key0": "Voltar",
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
        self.window.Close()
        return opcao

    def imprime_mensagem(self, mensagem):
        self.window = sg.Popup(
            mensagem, title="Mensagem", font=("Helvetica", 18))

    def obtem_dados_voto(self):
        confirma = False
        layout = [
            [self.text('Votação', fontSize=25)],
            [self.text('Número do reitor:                      '),
                self.input_text(data="", key='reitor')],
            [self.text('Número do pró-reitor de graduação:     '),
                self.input_text(data="", key='pro_grad')],
            [self.text('Número do pró-reitor de extensão:      '),
                self.input_text(data="", key='pro_ext')],
            [self.text('Número do pró-reitor de pesquisa:      '),
                self.input_text(data="", key='pro_pesquisa')],
            [self.confirm_button(), self.cancel_button('Voltar')]
        ]
        self.window = sg.Window(
            'Votação').Layout(layout)
        while True:
            button, values = self.window.Read()
            if button in (None, 'Voltar'):
                self.window.Close()
                return None
            reitor = values["reitor"]
            pro_grad = values["pro_grad"]
            pro_ext = values["pro_ext"]
            pro_pesquisa = values["pro_pesquisa"]
            confirma = self.confirma_voto()
            if confirma:
                break
        self.window.Close()
        return {"reitor": reitor, "pro_grad": pro_grad,
                "pro_ext": pro_ext, "pro_pesquisa": pro_pesquisa}

    def confirma_voto(self):
        layout = [
            [self.text('Confirma o voto?', fontSize=25)],
            [self.confirm_button(), self.confirm_button('Corrigir', color="red")]
        ]
        window = sg.Window(
            'Confirmação de voto').Layout(layout)
        button, values = window.Read()
        if button in (None, 'Corrigir'):
            window.Close()
            return False
        window.Close()
        return True

    def define_segundo_turno(self):
        self.init_components({
            "title": "Definição de Turno",
            "key1": "Primeiro Turno",
            "key2": "Segundo Turno",
            "key3": "",
            "key4": "",
            "key5": "",
            "key0": "Voltar",
        })
        button, values = self.window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.window.Close()
        return opcao

    def escreve_resultados(self, candidatos):
        with open("resultados.txt", "w") as file:
            for candidato in candidatos:
                tipo_candidato = self.verifica_tipo_candidato(candidato)
                file.write(f"O {tipo_candidato} vencedor é: \n")

                file.write(f"Nome: {candidato.nome} \n")
                file.write(f"Número: {candidato.numero} \n")
                file.write(f"Pontuação: {candidato.pontuacao}\n")
                file.write(
                    f"Quantidade de votos de aluno: {candidato.votos_aluno}\n")
                file.write(
                    f"Quantidade de votos de professor: {candidato.votos_professor}\n")
                file.write(
                    f"Quantidade de votos de servidor: {candidato.votos_servidor}\n")
                file.write("-"*20)
                file.write("\n")
                file.write(f"Nome da chapa: {candidato.chapa.nome}\n")
                file.write(f"ID da chapa: {candidato.chapa.id}\n")
                file.write("-"*20)
                file.write("\n\n")

    def escreve_quantidades(self):
        with open("quantidade_votos.txt", "w") as file:
            file.write(
                f"Total de votos nulos/inválidos: {self.__controlador_urna.urna.quantidade_votos_invalidos}\n\n")
            for candidato in self.__controlador_urna.urna.candidatos:
                tipo_candidato = self.verifica_tipo_candidato(candidato)
                file.write(f"O {tipo_candidato}\n")
                file.write(f"De nome: {candidato.nome}\n")
                file.write(f"De número: {candidato.numero}\n")
                file.write(
                    f"Concorrendo pela chapa de nome: {candidato.chapa.nome}\n")
                file.write(f"Com ID de chapa: {candidato.chapa.id}\n\n")
                file.write(
                    f"Teve um total de {candidato.votos_aluno} voto(s) de aluno\n")
                file.write(
                    f"Um total de {candidato.votos_professor} voto(s) de professor\n")
                file.write(
                    f"E um total de {candidato.votos_servidor} voto(s) de servidor\n")
                file.write("-"*20)
                file.write("\n\n")

    def verifica_tipo_candidato(self, candidato):
        if isinstance(candidato, Reitor):
            return "reitor"
        if isinstance(candidato, ProReitor):
            if candidato.tipo_pro_reitor == TipoProReitor.GRADUACAO.value:
                return "pró-reitor de graduação"
            elif candidato.tipo_pro_reitor == TipoProReitor.EXTENSAO.value:
                return "pró-reitor de extensão"
            elif candidato.tipo_pro_reitor == TipoProReitor.PESQUISA.value:
                return "pró-reitor de pesquisa"
