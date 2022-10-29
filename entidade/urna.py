class Urna:
    def __init__(self, candidatos, eleitores: list):
        self.__candidatos = candidatos
        self.__eleitores = eleitores
        self.__homologada = False
        self.__turno = 1
        self.__votos = []
        self.__eleitores_votaram = []
        self.__quantidade_votos_invalidos = 0

    @property
    def candidatos(self) -> list:
        return self.__candidatos

    @property
    def eleitores(self) -> list:
        return self.__eleitores

    @property
    def votos(self) -> list:
        return self.__votos

    @property
    def homologada(self) -> bool:
        return self.__homologada

    @homologada.setter
    def homologada(self, homologada):
        self.__homologada = homologada

    @property
    def turno(self) -> int:
        return self.__turno

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    @property
    def quantidade_votos_invalidos(self) -> int:
        return self.__quantidade_votos_invalidos

    @quantidade_votos_invalidos.setter
    def quantidade_votos_invalidos(self, quantidade_votos_invalidos):
        self.__quantidade_votos_invalidos = quantidade_votos_invalidos

    @property
    def eleitores_votaram(self) -> list:
        return self.__eleitores_votaram
