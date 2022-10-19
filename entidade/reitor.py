from entidade.candidato import Candidato
from entidade.chapa import Chapa


class Reitor(Candidato):
    def __init__(self, nome: str, numero: int, chapa: Chapa):
        super().__init__(nome, numero, chapa)
