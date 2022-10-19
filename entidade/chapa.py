class Chapa:
    def __init__(self, nome: str, id: int):
        self.__nome = nome
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id
