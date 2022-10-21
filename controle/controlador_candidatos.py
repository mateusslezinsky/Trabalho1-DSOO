from limite.tela_candidato import TelaCandidato
from controle.controlador_reitores import ControladorReitores
from controle.controlador_pro_reitores import ControladorProReitores


class ControladorCandidatos:
    def __init__(self, controlador_sistema, controlador_chapas):
        self.__tela_candidato = TelaCandidato(self)
        self.__controlador_reitores = ControladorReitores(self)
        self.__controlador_pro_reitores = ControladorProReitores()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_chapas = controlador_chapas
        self.opcao_crud = 0

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def controlador_chapas(self):
        return self.__controlador_chapas

    def escolhe_tipo_candidato(self):
        # operacao_escolhida = self.__tela_candidato.tela_candidato_opcoes()
        if self.opcao_crud == 1:
            opcoes = {0: self.abre_tela,
                      1: self.__controlador_reitores.cadastra_reitor,
                      2: self.__controlador_pro_reitores.cadastra_pro_reitor}
        elif self.opcao_crud == 2:
            opcoes = {0: self.abre_tela,
                      1: self.__controlador_reitores.altera_reitor,
                      2: self.__controlador_pro_reitores.altera_pro_reitor}
        elif self.opcao_crud == 3:
            opcoes = {0: self.abre_tela,
                      1: self.__controlador_reitores.consulta_reitor,
                      2: self.__controlador_pro_reitores.consulta_pro_reitor}
        elif self.opcao_crud == 4:
            opcoes = {0: self.abre_tela,
                      1: self.__controlador_reitores.exclui_reitor,
                      2: self.__controlador_pro_reitores.exclui_pro_reitor}
        while True:
            try:
                opcao_escolhida = self.__tela_candidato.tela_escolha_cadastro()
                opcoes[opcao_escolhida]()
            except(KeyError, ValueError, KeyboardInterrupt):
                self.__controlador_sistema.tela_sistema.lida_com_erro()

    # Teste de cadastro Reitor + Chapa
    # novoReitor = Reitor("a", 2, self.__controlador_chapa.chapas[0])

    def abre_tela(self):
        self.__controlador_sistema.tela_crud(
            {"cadastro": self.escolhe_tipo_candidato,
             "alterar": self.escolhe_tipo_candidato,
             "consultar": self.escolhe_tipo_candidato,
             "excluir": self.escolhe_tipo_candidato,
             "tela": self.__tela_candidato.tela_candidato_opcoes
             })
