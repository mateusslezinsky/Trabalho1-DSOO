from enum import Enum


class TipoEleitor(Enum):
    ALUNO = 1
    PROFESSOR = 2
    SERVIDOR = 3


class Eleitor:
    def __init__(self, nome: str, cpf: int, tipo_eleitor: TipoEleitor):
        self.__nome = nome
        self.__cpf = cpf
        self.__tipo_eleitor = tipo_eleitor

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def tipo_eleitor(self):
        return self.__tipo_eleitor

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf

    @tipo_eleitor.setter
    def tipo_eleitor(self, tipo_eleitor):
        self.__tipo_eleitor = tipo_eleitor
