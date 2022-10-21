from limite.tela_eleitor import TelaEleitor


class ControladorEleitores:
    def __init__(self, controlador_sistema):
        self.__tela_eleitor = TelaEleitor()
        self.__controlador_sistema = controlador_sistema

    def cadastra_eleitor(self):
        pass

    def altera_eleitor(self):
        pass

    def consulta_eleitor(self):
        pass

    def exclui_eleitor(self):
        pass

    def abre_tela(self):
        self.__controlador_sistema.tela_crud(
            {"cadastro": self.cadastra_eleitor,
             "alterar": self.altera_eleitor,
             "consultar": self.consulta_eleitor,
             "excluir": self.exclui_eleitor,
             "tela": self.__tela_eleitor.tela_eleitor_opcoes
             })
