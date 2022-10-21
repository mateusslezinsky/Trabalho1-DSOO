from limite.tela_sistema import TelaSistema
from controle.controlador_chapas import ControladorChapas
from controle.controlador_candidatos import ControladorCandidatos


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema(self)
        self.__controlador_chapa = ControladorChapas(self)
        self.__controlador_candidato = ControladorCandidatos(
            self, self.__controlador_chapa)

    @property
    def tela_sistema(self):
        return self.__tela_sistema

    @property
    def controlador_candidato(self):
        return self.__controlador_candidato

    def inicializa_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        opcoes = {0: self.encerra_sistema,
                  1: self.__controlador_chapa.abre_tela,
                  2: self.__controlador_candidato.abre_tela}

        while True:
            try:
                opcao_escolhida = self.__tela_sistema.tela_principal()
                opcoes[opcao_escolhida]()
            except (KeyError, ValueError, KeyboardInterrupt):
                self.__tela_sistema.lida_com_erro()

    def tela_crud(self, attr):

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
