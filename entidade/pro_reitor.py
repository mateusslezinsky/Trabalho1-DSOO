from entidade.chapa import Chapa
from entidade.candidato import Candidato
from enum import Enum


class TipoProReitor(Enum):
    GRADUACAO = 1
    EXTENSAO = 2
    PESQUISA = 3


class ProReitor(Candidato):
    def __init__(self, nome: str, numero: int, chapa: Chapa, tipo_pro_reitor: TipoProReitor):
        super().__init__(nome, numero, chapa)

        # tipo é int sendo:
        # 1 - Pró-reitoria de Graduação
        # 2 - Pró-reitoria de Extensão
        # 3 - Pró-reitoria de Pesquisa

        self.__tipo_pro_reitor = tipo_pro_reitor

    @property
    def tipo_pro_reitor(self):
        return self.__tipo_pro_reitor

    @tipo_pro_reitor.setter
    def tipo_pro_reitor(self, tipo_pro_reitor):
        self.__tipo_pro_reitor = tipo_pro_reitor
