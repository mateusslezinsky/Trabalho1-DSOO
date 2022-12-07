from entidade.candidato import Candidato
from persistencia.DAO import DAO
from pathlib import Path


class CandidatoDAO(DAO):
    def __init__(self):
        super().__init__(Path("./persistencia/candidatos.pkl"))

    def add(self, candidato: Candidato):
        if isinstance(candidato, Candidato):
            super().add(candidato.numero, candidato)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        return super().remove(key)
