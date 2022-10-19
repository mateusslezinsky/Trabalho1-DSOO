from candidato import Candidato


class Chapa:
    # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
    def __init__(self, nome: str, id: int, candidatos: [Candidato]):
        self.__nome = nome
        self.__id = id
        if isinstance(candidatos, Candidato):
            self.__candidatos.append(candidatos)

    @property
    def nome(self):
        return self.__nome

    @property
    def id(self):
        return self.__id

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @id.setter
    def id(self, id: str):
        self.__id = id
