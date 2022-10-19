from chapa import Chapa


class Candidato:
    # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
    def __init__(self, nome: str, numero: int, chapa: Chapa):
        self.__nome = nome
        self.__numero = numero
        if isinstance(chapa, Chapa):
            self.__chapa = chapa

    @property
    def nome(self):
        return self.__nome

    @property
    def numero(self):
        return self.__numero

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero
