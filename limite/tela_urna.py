class TelaUrna:
    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna

    def imprime_mensagem(self, mensagem):
        print(mensagem)

    def obtem_dados_voto(self):
        reitor = input(
            "Digite o número do reitor que deseja votar: ")
        pro_grad = input(
            "Digite o número do pró-reitor de graduação que deseja votar: ")
        pro_ext = input(
            "Digite o número do pró-reitor de extensão que deseja votar: ")
        pro_pesquisa = input(
            "Digite o número do pró-reitor de pesquisa que deseja votar: ")

        return {"reitor": reitor, "pro_grad": pro_grad,
                "pro_ext": pro_ext, "pro_pesquisa": pro_pesquisa}
