from limite.tela_chapa import TelaChapa


class ControladorChapa:
    def __init__(self, controlador_sistema):
        self.__tela_chapa = TelaChapa()
        self.__controlador_sistema = controlador_sistema

    def cadastro_chapa(self):
        chapa = self.__tela_chapa.cadastrar_chapa()

    def abre_tela(self):
        opcoes_chapa = {1: self.cadastro_chapa,
                        0: self.__controlador_sistema.abre_tela}
        while True:
            try:
                opcoes_chapa[self.__tela_chapa.tela_chapa_opcoes()]()
            except KeyError:
                print("\nErro da opção da chapa!")
