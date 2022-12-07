class Urna:
    def __init__(self, candidatos: list, eleitores: list):
        self.__candidatos = candidatos
        self.__eleitores = eleitores
        self.__homologada = False
        self.__votacao_encerrada = False
        self.__resultados_calculados = False
        self.__votos = []
        self.__eleitores_votaram = []
        self.__quantidade_votos_invalidos = 0
        self.id = 1

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
    def quantidade_votos_invalidos(self) -> int:
        return self.__quantidade_votos_invalidos

    @quantidade_votos_invalidos.setter
    def quantidade_votos_invalidos(self, quantidade_votos_invalidos):
        self.__quantidade_votos_invalidos = quantidade_votos_invalidos

    @property
    def eleitores_votaram(self) -> list:
        return self.__eleitores_votaram

    @property
    def votacao_encerrada(self):
        return self.__votacao_encerrada

    @votacao_encerrada.setter
    def votacao_encerrada(self, votacao_encerrada):
        self.__votacao_encerrada = votacao_encerrada

    @property
    def resultados_calculados(self):
        return self.__resultados_calculados

    @resultados_calculados.setter
    def resultados_calculados(self, resultados_calculados):
        self.__resultados_calculados = resultados_calculados
