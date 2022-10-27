class Voto:
    def __init__(self, reitor, pro_grad, pro_ext, pro_pesquisa, tipo_eleitor):
        self.__reitor = reitor
        self.__pro_grad = pro_grad
        self.__pro_ext = pro_ext
        self.__pro_pesquisa = pro_pesquisa
        self.__tipo_eleitor = tipo_eleitor

    @property
    def reitor(self):
        return self.__reitor

    @property
    def pro_grad(self):
        return self.__pro_grad

    @property
    def pro_ext(self):
        return self.__pro_ext

    @property
    def pro_pesquisa(self):
        return self.__pro_pesquisa

    @property
    def tipo_eleitor(self):
        return self.__tipo_eleitor
