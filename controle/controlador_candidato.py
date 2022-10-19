from limite.tela_candidato import TelaCandidato
from entidade.reitor import Reitor


class ControladorCandidato:
    def __init__(self, controlador_sistema, controlador_chapa):
        self.__tela_candidato = TelaCandidato()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_chapa = controlador_chapa

    def cadastra_candidato(self):
        # Teste de cadastro Reitor + Chapa
        novoReitor = Reitor("a", 2, self.__controlador_chapa.chapas[0])


    def altera_candidato(self):
        pass

    def consulta_candidato(self):
        pass

    def exclui_candidato(self):
        pass

    def abre_tela(self):
        self.__controlador_sistema.tela_crud(
            {"cadastro": self.cadastra_candidato,
             "alterar": self.altera_candidato,
             "consultar": self.consulta_candidato,
             "excluir": self.exclui_candidato,
             "tela": self.__tela_candidato.tela_candidato_opcoes
             })
