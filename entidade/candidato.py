from abc import ABC, abstractmethod
from entidade.chapa import Chapa


class Candidato(ABC):
    @abstractmethod
    def __init__(self, nome: str, numero: int, chapa: Chapa):
        self.__nome = nome
        self.__numero = numero
        if isinstance(chapa, Chapa):
            self.__chapa = chapa
        self.__pontuacao = 0
        self.__votos_aluno = 0
        self.__votos_professor = 0
        self.__votos_servidor = 0

    def __lt__(self, other):
        return self.__numero < other.numero

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

    @property
    def chapa(self):
        return self.__chapa

    @chapa.setter
    def chapa(self, chapa: Chapa):
        self.__chapa = chapa

    @property
    def pontuacao(self):
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, pontuacao):
        self.__pontuacao = pontuacao

    @property
    def votos_aluno(self):
        return self.__votos_aluno

    @votos_aluno.setter
    def votos_aluno(self, votos_aluno):
        self.__votos_aluno = votos_aluno

    @property
    def votos_professor(self):
        return self.__votos_professor

    @votos_professor.setter
    def votos_professor(self, votos_professor):
        self.__votos_professor = votos_professor

    @property
    def votos_servidor(self):
        return self.__votos_servidor

    @votos_servidor.setter
    def votos_servidor(self, votos_servidor):
        self.__votos_servidor = votos_servidor
