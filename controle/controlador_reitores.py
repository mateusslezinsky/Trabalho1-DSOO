from entidade import reitor
from limite.tela_reitor import TelaReitor
from entidade.reitor import Reitor


class ControladorReitores:
    def __init__(self, controlador_candidatos):
        self.__reitores = []
        self.__controlador_candidatos = controlador_candidatos
        self.__tela_reitor = TelaReitor(self)

    @property
    def controlador_candidatos(self):
        return self.__controlador_candidatos

    def checa_se_ja_existe(self, id_a_checar):
        for reitor in self.__reitores:
            if reitor.numero == id_a_checar:
                return True
        else:
            return False

    def cadastra_reitor(self):
        dados_a_cadastrar = self.__tela_reitor.cadastrar_reitor()

        objeto_chapa = self.__controlador_candidatos.controlador_chapas.consulta_chapa(
            mostrar=False)
        if objeto_chapa is not None:
            reitor_a_cadastrar = Reitor(
                dados_a_cadastrar["nome"], dados_a_cadastrar["numero"], objeto_chapa)
            self.__reitores.append(reitor_a_cadastrar)

    def altera_reitor(self):
        reitor_consultado = self.consulta_reitor(mostrar=False)
        if reitor_consultado is not None:
            dados_reitor = self.__tela_reitor.cadastrar_reitor()
            objeto_chapa = self.__controlador_candidatos.controlador_chapas.consulta_chapa(
                mostrar=False)
            if objeto_chapa is not None:
                for reitor in self.__reitores:
                    if reitor.numero == reitor_consultado.numero:
                        reitor.nome = dados_reitor["nome"]
                        reitor.numero = dados_reitor["numero"]
                        reitor.chapa = objeto_chapa

    def consulta_reitor(self, mostrar=True):
        reitor_consultado = self.__tela_reitor.consulta_reitor()
        for reitor in self.__reitores:
            if reitor.numero == reitor_consultado:
                if mostrar:
                    self.__tela_reitor.imprime_dados(reitor)
                return reitor
        else:
            self.__tela_reitor.imprime_dados(None)

    def exclui_reitor(self):
        reitor_consultado = self.consulta_reitor()
        if reitor_consultado is not None:
            for reitor in self.__reitores:
                if reitor.numero == reitor_consultado.numero:
                    self.__reitores.remove(reitor)
                    self.__tela_reitor.remove_reitor()
