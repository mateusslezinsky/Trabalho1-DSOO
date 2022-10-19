from limite.tela_chapa import TelaChapa
from entidade.chapa import Chapa


class ControladorChapa:
    def __init__(self, controlador_sistema):
        self.__chapas = []
        self.__tela_chapa = TelaChapa()
        self.__controlador_sistema = controlador_sistema

    def cadastro_chapa(self):
        chapa_dict = self.__tela_chapa.cadastrar_chapa(self.__chapas)
        nova_chapa = Chapa(chapa_dict["nome"], chapa_dict["id"])
        self.__chapas.append(nova_chapa)

    def alterar_chapa(self):
        chapa_consultada = self.consulta_chapa()
        if chapa_consultada is not None:
            dados_tela_chapa = self.__tela_chapa.cadastrar_chapa(self.__chapas)
            for chapa in self.__chapas:
                if chapa.id == chapa_consultada.id:
                    chapa.nome = dados_tela_chapa["nome"]
                    chapa.id = dados_tela_chapa["id"]

    def consulta_chapa(self):
        id_a_consultar = self.__tela_chapa.consultar_chapa(self.__chapas)
        if len(self.__chapas) > 0:
            for chapa in self.__chapas:
                if chapa.id == id_a_consultar:
                    self.__tela_chapa.mostra_chapa(chapa)
                    return chapa
            else:
                self.__tela_chapa.mostra_chapa(None)
        else:
            self.__tela_chapa.mostra_chapa(None)

    def exclui_chapa(self):
        chapa_consultada = self.consulta_chapa()
        if chapa_consultada is not None:
            for chapa in self.__chapas:
                if chapa.id == chapa_consultada.id:
                    self.__chapas.remove(chapa)
                    self.__tela_chapa.exclui_chapa()

    def abre_tela(self):
        opcoes_chapa = {1: self.cadastro_chapa,
                        2: self.alterar_chapa,
                        3: self.consulta_chapa,
                        4: self.exclui_chapa,
                        0: self.__controlador_sistema.abre_tela}
        while True:
            try:
                opcoes_chapa[self.__tela_chapa.tela_chapa_opcoes(
                    self.__controlador_sistema.tela_sistema)]()
            except (KeyError, ValueError, KeyboardInterrupt):
                print("\nOpção inválida!")
