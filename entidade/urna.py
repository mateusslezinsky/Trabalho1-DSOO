class Urna:
    def __init__(self, candidatos, eleitores: list):
        self.__candidatos = candidatos
        self.__eleitores = eleitores
        self.__homologada = False
        self.__votos = []
        self.__turno = 1

    @property
    def candidatos(self) -> list:
        return self.__candidatos

    @property
    def eleitores(self) -> list:
        return self.__eleitores

    @property
    def homologada(self) -> bool:
        return self.__homologada

    @homologada.setter
    def homologada(self, homologada):
        self.__homologada = homologada

    @property
    def votos(self) -> list:
        return self.__votos

    @property
    def turno(self) -> int:
        return self.__turno

    @turno.setter
    def turno(self, turno):
        self.__turno = turno
