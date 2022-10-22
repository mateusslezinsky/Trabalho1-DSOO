from limite.tela_candidato import TelaCandidato
from entidade.reitor import Reitor
from entidade.pro_reitor import ProReitor, TipoProReitor


class ControladorCandidatos:
    def __init__(self, controlador_sistema, controlador_chapas):
        self.__tela_candidato = TelaCandidato(self)
        self.__reitores = []
        self.__pro_reitores = []
        self.__controlador_sistema = controlador_sistema
        self.__controlador_chapas = controlador_chapas
        self.opcao_crud = 0
        self.opcao_tipo_candidato = 0

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def controlador_chapas(self):
        return self.__controlador_chapas

    @property
    def tela_candidato(self):
        return self.__tela_candidato

    @property
    def reitores(self):
        return self.__reitores

    @property
    def pro_reitores(self):
        return self.__pro_reitores

    def escolhe_tipo_candidato(self):
        if self.opcao_crud == 1:
            opcoes = {0: self.abre_tela,
                      1: self.cadastra_candidato,
                      2: self.cadastra_candidato}
        elif self.opcao_crud == 2:
            opcoes = {0: self.abre_tela,
                      1: self.altera_candidato,
                      2: self.altera_candidato}
        elif self.opcao_crud == 3:
            opcoes = {0: self.abre_tela,
                      1: self.consulta_candidato,
                      2: self.consulta_candidato}
        elif self.opcao_crud == 4:
            opcoes = {0: self.abre_tela,
                      1: self.exclui_candidato,
                      2: self.exclui_candidato}
        while True:
            try:
                opcao_escolhida = self.__tela_candidato.tela_escolha_cadastro()
                self.opcao_tipo_candidato = opcao_escolhida
                opcoes[opcao_escolhida]()
            except(KeyError, ValueError, KeyboardInterrupt):
                self.__controlador_sistema.tela_sistema.lida_com_erro()

    def abre_tela(self):
        self.__controlador_sistema.tela_crud(
            {"cadastro": self.escolhe_tipo_candidato,
             "alterar": self.escolhe_tipo_candidato,
             "consultar": self.escolhe_tipo_candidato,
             "excluir": self.escolhe_tipo_candidato,
             "tela": self.__tela_candidato.tela_candidato_opcoes
             })

    def checa_se_ja_existe(self, id_a_checar, lista):
        for item in lista:
            if item.numero == id_a_checar:
                return True
        else:
            return False

    def cadastra_candidato(self):
        candidato = self.__tela_candidato.cadastrar_candidato()
        objeto_chapa = self.__controlador_chapas.consulta_chapa(
            mostrar=False)
        if objeto_chapa is not None:
            if self.opcao_tipo_candidato == 1:
                reitor_a_cadastrar = Reitor(
                    candidato["nome"], candidato["numero"], objeto_chapa)
                self.__reitores.append(reitor_a_cadastrar)
            elif self.opcao_tipo_candidato == 2:
                if candidato["tipo_pro_reitor"] == 1:
                    pro_reitor_a_cadastrar = ProReitor(
                        candidato["nome"], candidato["numero"], objeto_chapa, TipoProReitor.GRADUACAO.value)
                elif candidato["tipo_pro_reitor"] == 2:
                    pro_reitor_a_cadastrar = ProReitor(
                        candidato["nome"], candidato["numero"], objeto_chapa, TipoProReitor.EXTENSAO.value)
                elif candidato["tipo_pro_reitor"] == 3:
                    pro_reitor_a_cadastrar = ProReitor(
                        candidato["nome"], candidato["numero"], objeto_chapa, TipoProReitor.PESQUISA.value)
                self.__pro_reitores.append(
                    pro_reitor_a_cadastrar)

    def altera_candidato(self):
        candidato_consultado = self.consulta_candidato(
            mostrar=False)
        if candidato_consultado is not None:
            dados_candidato = self.__tela_candidato.cadastrar_candidato()
            objeto_chapa = self.controlador_chapas.consulta_chapa(
                mostrar=False)
            if objeto_chapa is not None:
                if self.opcao_tipo_candidato == 1:
                    lista = self.__reitores
                elif self.opcao_tipo_candidato == 2:
                    lista = self.__pro_reitores
                for candidato in lista:
                    if candidato.numero == candidato_consultado.numero:
                        candidato.nome = dados_candidato["nome"]
                        candidato.numero = dados_candidato["numero"]
                        if self.opcao_tipo_candidato == 2:
                            candidato.tipo_pro_reitor = dados_candidato["tipo_pro_reitor"]
                        candidato.chapa = objeto_chapa

    def consulta_candidato(self, mostrar=True):
        numero_consultado = self.tela_candidato.consulta_candidato()
        if self.opcao_tipo_candidato == 1:
            lista = self.__reitores
        elif self.opcao_tipo_candidato == 2:
            lista = self.__pro_reitores
        for candidato in lista:
            if candidato.numero == numero_consultado:
                if mostrar:
                    self.tela_candidato.imprime_dados(
                        candidato)
                return candidato
        else:
            self.tela_candidato.imprime_dados(
                None)

    def exclui_candidato(self):
        candidato_consultado = self.consulta_candidato()
        if candidato_consultado is not None:
            if self.opcao_tipo_candidato == 1:
                lista = self.__reitores
            elif self.opcao_tipo_candidato == 2:
                lista = self.__pro_reitores
            for candidato in lista:
                if candidato.numero == candidato_consultado.numero:
                    lista.remove(candidato)
                    self.__tela_candidato.remove_candidato()
