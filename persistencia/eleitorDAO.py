from entidade.eleitor import Eleitor
from persistencia.DAO import DAO
from pathlib import Path


class EleitorDAO(DAO):
    def __init__(self):
        super().__init__(Path("./persistencia/eleitores.pkl"))

    def add(self, eleitor: Eleitor):
        if isinstance(eleitor, Eleitor):
            super().add(eleitor.cpf, eleitor)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        return super().remove(key)
