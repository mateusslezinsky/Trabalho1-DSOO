from entidade.urna import Urna
from limite.tela_urna import TelaUrna


class ControladorUrna:
    def __init__(self, controlador_sistema, controlador_candidatos, controlador_eleitores) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__controlador_candidatos = controlador_candidatos
        self.__controlador_eleitores = controlador_eleitores
        self.__tela_urna = TelaUrna()
        self.__urna = None

    @property
    def urna(self):
        return self.__urna

    @urna.setter
    def urna(self, urna):
        self.__urna = urna

    def homologacao(self):
        # Lista exemplo para fins de teste de homologação de urna. Relacionado a eleitores
        sample_list = [1, 2, 3]
        if (len(sample_list) > 0) and (len(self.__controlador_candidatos.reitores) > 0 and len(self.__controlador_candidatos.pro_reitores)):
            urna = Urna(self.__controlador_candidatos.reitores,
                        self.__controlador_candidatos.pro_reitores, sample_list)
            if len(urna.eleitores) > 0 and len(urna.candidatos):
                urna.homologada = True
                self.__urna = urna
                self.__tela_urna.imprime_mensagem(
                    "A urna foi homologada com sucesso. O voto pode ser realizado.")
        else:
            self.__tela_urna.imprime_mensagem(
                "Não foi possível homologar a urna! Para isso são necessários cadastros de eleitores e candidatos.")

    def votacao(self):
        if self.__urna is None:
            self.__tela_urna.imprime_mensagem(
                "Para realizar a votação é necessário que a urna esteja homologada!")
        else:
            self.__tela_urna.imprime_mensagem("Voto será realizado")
