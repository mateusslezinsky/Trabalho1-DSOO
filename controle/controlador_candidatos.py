from limite.tela_candidato import TelaCandidato


class ControladorCandidatos:
    def __init__(self, controlador_sistema):
        self.__tela_candidato = TelaCandidato()
        self.__controlador_sistema = controlador_sistema

    def cadastro_candidato(self):
        chapa = self.__tela_candidato.cadastrar_candidato()

    def abre_tela(self):
        opcoes_candidato = {1: self.cadastro_candidato,
                            0: self.__controlador_sistema.abre_tela}
        while True:
            try:
                opcoes_candidato[self.__tela_candidato.tela_candidato_opcoes(
                                 self.__controlador_sistema.tela_sistema)]()
            except KeyError:
                print("\nErro da opção de candidato!")
