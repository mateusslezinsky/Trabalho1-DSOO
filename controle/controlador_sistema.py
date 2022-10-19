from limite.tela_sistema import TelaSistema
from controle.controlador_chapa import ControladorChapa
from controle.controlador_candidato import ControladorCandidato


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_chapa = ControladorChapa(self)
        self.__controlador_candidato = ControladorCandidato(self)

    @property
    def tela_sistema(self):
        return self.__tela_sistema

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
                print("\nDigite uma opção válida!")
