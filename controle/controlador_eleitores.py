from limite.tela_eleitor import TelaEleitor
from entidade.eleitor import Eleitor, TipoEleitor
from persistencia.eleitorDAO import EleitorDAO


class ControladorEleitores:
    def __init__(self, controlador_sistema):
        self.__eleitores = EleitorDAO()
        self.__tela_eleitor = TelaEleitor(self)
        self.__controlador_sistema = controlador_sistema

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def eleitores(self):
        return self.__eleitores

    @eleitores.setter
    def eleitores(self, eleitores):
        self.__eleitores = eleitores

    def cadastra_eleitor(self):
        eleitor_dict = self.__tela_eleitor.cadastra_eleitor()
        if eleitor_dict is None:
            return
        elif len(eleitor_dict["nome"]) == 0:
            self.__tela_eleitor.error("Nome inexistente!")
            return
        elif len(eleitor_dict["cpf"]) == 0:
            self.__tela_eleitor.error("CPF inexistente!")
            return
        for eleitor in self.__eleitores.get_all():
            if eleitor_dict["cpf"] == eleitor.cpf:
                self.__tela_eleitor.error("CPF já cadastrado!")
                return
        novo_eleitor = Eleitor(
            eleitor_dict["nome"], eleitor_dict["cpf"], eleitor_dict["tipo_eleitor"])
        self.__eleitores.add(novo_eleitor)

    def altera_eleitor(self):
        eleitor_consultado = self.consulta_eleitor(mostrar=False)
        if eleitor_consultado is not None:
            dados_eleitor = self.__tela_eleitor.altera_eleitor(eleitor_consultado)
            if dados_eleitor is None:
                return
            for eleitor in self.__eleitores.get_all():
                if eleitor_consultado.cpf == dados_eleitor["cpf"]:
                    break
                elif dados_eleitor["cpf"] == eleitor.cpf:
                    self.__tela_eleitor.error("CPF já cadastrado!")
                    return
            for eleitor in list(self.__eleitores.get_all()):
                if eleitor.cpf == eleitor_consultado.cpf:
                    self.__eleitores.remove(eleitor.cpf)
                    eleitor_a_alterar = Eleitor(
                            dados_eleitor["nome"], dados_eleitor["cpf"], dados_eleitor["tipo_eleitor"])
                    self.__eleitores.add(eleitor_a_alterar)

    def consulta_eleitor(self, mostrar=True):
        id_a_consultar = self.__tela_eleitor.consulta_eleitor()
        if id_a_consultar is None:
            return
        for eleitor in self.__eleitores.get_all():
            if eleitor.cpf == id_a_consultar:
                if mostrar:
                    self.__tela_eleitor.mostra_eleitor(eleitor)
                return eleitor
        else:
            self.__tela_eleitor.mostra_eleitor(None)

    def exclui_eleitor(self):
        eleitor_consultado = self.consulta_eleitor(mostrar=False)
        if eleitor_consultado is not None:
            for eleitor in list(self.__eleitores.get_all()):
                if eleitor.cpf == eleitor_consultado.cpf:
                    self.__eleitores.remove(eleitor.cpf)
                    self.__tela_eleitor.exclui_eleitor(eleitor)

    def abre_tela(self):
        self.__controlador_sistema.tela_crud(
            {"cadastro": self.cadastra_eleitor,
             "alterar": self.altera_eleitor,
             "consultar": self.consulta_eleitor,
             "excluir": self.exclui_eleitor,
             "tela": self.__tela_eleitor.tela_eleitor_opcoes
             })

    def checa_se_ja_existe(self, id_a_checar, lista):
        for item in lista:
            if item.cpf == id_a_checar:
                return True
        else:
            return False
