from limite.tela_sistema import TelaSistema
from controle.controlador_chapa import ControladorChapa


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_chapa = ControladorChapa(self)

    def inicializa_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def controlador_chapa(self):
        return self.__controlador_chapa.abre_tela()

    def abre_tela(self):
        opcoes = {0: self.encerra_sistema, 1: self.controlador_chapa}

        while True:
            try:
                opcao_escolhida = self.__tela_sistema.tela_principal()
                opcoes[opcao_escolhida]()
            except KeyError:
                print("\nDigite uma opção válida!")
