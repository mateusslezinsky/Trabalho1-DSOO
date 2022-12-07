from limite.tela_sistema import TelaSistema
from controle.controlador_chapas import ControladorChapas
from controle.controlador_candidatos import ControladorCandidatos
from controle.controlador_urna import ControladorUrna
from controle.controlador_eleitores import ControladorEleitores


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema(self)
        self.__controlador_chapas = ControladorChapas(self)
        self.__controlador_candidatos = ControladorCandidatos(
            self, self.__controlador_chapas)
        self.__controlador_eleitores = ControladorEleitores(self)
        self.__controlador_urna = ControladorUrna(
            self, self.__controlador_candidatos, self.__controlador_eleitores)

    @property
    def tela_sistema(self):
        return self.__tela_sistema

    @property
    def controlador_candidatos(self):
        return self.__controlador_candidatos

    @property
    def controlador_eleitores(self):
        return self.__controlador_eleitores

    @property
    def controlador_urna(self):
        return self.__controlador_urna

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        opcoes = {0: self.encerra_sistema,
                  1: self.__controlador_chapas.abre_tela,
                  2: self.__controlador_candidatos.abre_tela,
                  3: self.__controlador_eleitores.abre_tela,
                  4: self.__controlador_urna.abre_tela}

        while True:
            try:
                opcao_escolhida = self.__tela_sistema.tela_principal()
                opcoes[opcao_escolhida]()
            except (KeyError, ValueError, KeyboardInterrupt):
                self.__tela_sistema.lida_com_erro()

    def tela_crud(self, attr):
        if self.__controlador_urna.urna is not None and self.__controlador_urna.urna.homologada:
            self.__controlador_urna.tela_urna.imprime_mensagem(
                "Com a urna homologada não é possível fazer modificações!")
            return
        opcoes = {1: attr["cadastro"],
                  2: attr["alterar"],
                  3: attr["consultar"],
                  4: attr["excluir"],
                  0: self.abre_tela}
        while True:
            try:
                opcoes[attr["tela"]()]()
            except (KeyError, ValueError, KeyboardInterrupt):
                self.__tela_sistema.lida_com_erro()

    def redefine_sistema(self):
        self.__controlador_urna.urna = None
        self.__controlador_urna.votacao_encerrada = False
        self.__controlador_urna.resultados_calculados = False
        self.__tela_sistema.mensagem_redefine_sistema()
