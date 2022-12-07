from limite.tela_chapa import TelaChapa
from entidade.chapa import Chapa
from persistencia.chapaDAO import ChapaDAO


class ControladorChapas:
    def __init__(self, controlador_sistema):
        self.__chapas = ChapaDAO()
        self.__tela_chapa = TelaChapa(self)
        self.__controlador_sistema = controlador_sistema

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def chapas(self):
        return self.__chapas

    @chapas.setter
    def chapas(self, chapas):
        self.__chapas = chapas

    def cadastra_chapa(self):
        chapa_dict = self.__tela_chapa.cadastrar_chapa()
        if chapa_dict is None:
            return
        elif len(chapa_dict["nome"]) == 0:
            self.__tela_chapa.error("Nome inexistente!")
            return
        for chapa in self.__chapas.get_all():
            if chapa_dict["id"] == chapa.id:
                self.__tela_chapa.error("ID já cadastrado!")
                return
        nova_chapa = Chapa(chapa_dict["nome"], chapa_dict["id"])
        self.__chapas.add(nova_chapa)

    def altera_chapa(self):
        chapa_consultada = self.consulta_chapa(mostrar=False)
        if chapa_consultada is not None:
            dados_tela_chapa = self.__tela_chapa.alterar_chapa(
                chapa_consultada)
            for chapa in list(self.__chapas.get_all()):
                if chapa.id == chapa_consultada.id:
                    self.__chapas.remove(chapa.id)
                    nova_chapa = Chapa(
                        dados_tela_chapa["nome"], dados_tela_chapa["id"])
                    self.__chapas.add(nova_chapa)

    def consulta_chapa(self, mostrar=True):
        id_a_consultar = self.__tela_chapa.consultar_chapa()
        if id_a_consultar is None:
            return
        for chapa in self.__chapas.get_all():
            if chapa.id == id_a_consultar:
                if mostrar:
                    self.__tela_chapa.mostra_chapa(chapa)
                return chapa
        else:
            self.__tela_chapa.mostra_chapa(None)

    def exclui_chapa(self):
        chapa_consultada = self.consulta_chapa(mostrar=False)
        if chapa_consultada is not None:
            for chapa in list(self.__chapas.get_all()):
                if chapa.id == chapa_consultada.id:
                    self.__chapas.remove(chapa.id)
                    self.__tela_chapa.exclui_chapa(chapa)

    def abre_tela(self):
        self.__controlador_sistema.tela_crud(
            {"cadastro": self.cadastra_chapa,
             "alterar": self.altera_chapa,
             "consultar": self.consulta_chapa,
             "excluir": self.exclui_chapa,
             "tela": self.__tela_chapa.tela_chapa_opcoes
             })
