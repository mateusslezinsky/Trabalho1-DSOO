from enum import Enum


class TipoEleitor(Enum):
    ALUNO = 1
    PROFESSOR = 2
    SERVIDOR = 3


class Eleitor:
    def __init__(self, nome: str, cpf: int):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf
