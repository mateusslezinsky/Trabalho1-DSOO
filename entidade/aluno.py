from entidade.eleitor import Eleitor


class Aluno(Eleitor):
    def __init__(self, nome: str, cpf: int, matricula: int):
        super().__init__(nome, cpf)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: int):
        self.__matricula = matricula
