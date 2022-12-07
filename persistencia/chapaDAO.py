from entidade.chapa import Chapa
from persistencia.DAO import DAO
from pathlib import Path


class ChapaDAO(DAO):
    def __init__(self):
        super().__init__(Path("./persistencia/chapas.pkl"))

    def add(self, chapa: Chapa):
        if isinstance(chapa, Chapa):
            super().add(chapa.id, chapa)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        return super().remove(key)
