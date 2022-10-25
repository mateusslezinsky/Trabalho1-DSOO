from limite.tela_eleitor import TelaEleitor
from entidade.eleitor import Eleitor, TipoEleitor


class ControladorEleitores:
    def __init__(self, controlador_sistema):
        self.__eleitores = []
        self.__tela_eleitor = TelaEleitor(self)
        self.__controlador_sistema = controlador_sistema

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def eleitores(self):
        return self.__eleitores

    def cadastra_eleitor(self):
        eleitor_dict = self.__tela_eleitor.cadastra_eleitor()
        novo_eleitor = Eleitor(
            eleitor_dict["nome"], eleitor_dict["cpf"], eleitor_dict["tipo_eleitor"])
        self.__eleitores.append(novo_eleitor)

    def altera_eleitor(self):
        eleitor_consultado = self.consulta_eleitor()
        if eleitor_consultado is not None:
            dados_tela_eleitor = self.__tela_eleitor.cadastra_eleitor()
            for eleitor in self.__eleitores:
                if eleitor.cpf == eleitor_consultado.cpf:
                    eleitor.nome = dados_tela_eleitor["nome"]
                    eleitor.cpf = dados_tela_eleitor["cpf"]
                    eleitor.tipo_eleitor = dados_tela_eleitor["tipo_eleitor"]

    def consulta_eleitor(self, mostrar=True):
        id_a_consultar = self.__tela_eleitor.consulta_eleitor()
        if len(self.__eleitores) > 0:
            for eleitor in self.__eleitores:
                if eleitor.cpf == id_a_consultar:
                    if mostrar:
                        self.__tela_eleitor.mostra_eleitor(eleitor)
                    return eleitor
            else:
                self.__tela_eleitor.mostra_eleitor(None)
        else:
            self.__tela_eleitor.mostra_eleitor(None)

    def exclui_eleitor(self):
        eleitor_consultado = self.consulta_eleitor()
        if eleitor_consultado is not None:
            for eleitor in self.__eleitores:
                if eleitor.cpf == eleitor_consultado.cpf:
                    self.__eleitores.remove(eleitor)
                    self.__tela_eleitor.exclui_eleitor()

    def abre_tela(self):
        self.__controlador_sistema.tela_crud(
            {"cadastro": self.cadastra_eleitor,
             "alterar": self.altera_eleitor,
             "consultar": self.consulta_eleitor,
             "excluir": self.exclui_eleitor,
             "tela": self.__tela_eleitor.tela_eleitor_opcoes
             })
