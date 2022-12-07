from entidade.urna import Urna
from persistencia.DAO import DAO
from pathlib import Path


class UrnaDAO(DAO):
    def __init__(self):
        super().__init__(Path("./persistencia/urna.pkl"))

    def add(self, urna: Urna):
        if isinstance(urna, Urna):
            super().add(urna.id, urna)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        return super().remove(key)
