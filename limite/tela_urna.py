class TelaUrna:
    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna

    def imprime_mensagem(self, mensagem):
        print(mensagem)

    def obtem_dados_voto(self):
        reitor = input(
            "Digite o número do reitor que deseja votar: ")
        reitor = self.confirma_voto(reitor, "reitor")
        pro_grad = input(
            "Digite o número do pró-reitor de graduação que deseja votar: ")
        pro_grad = self.confirma_voto(pro_grad, "pró-reitor de graduação")

        pro_ext = input(
            "Digite o número do pró-reitor de extensão que deseja votar: ")
        pro_ext = self.confirma_voto(pro_ext, "pró-reitor de extensão")
        pro_pesquisa = input(
            "Digite o número do pró-reitor de pesquisa que deseja votar: ")
        pro_pesquisa = self.confirma_voto(
            pro_pesquisa, "pró-reitor de pesquisa")

        return {"reitor": reitor, "pro_grad": pro_grad,
                "pro_ext": pro_ext, "pro_pesquisa": pro_pesquisa}

    def confirma_voto(self, candidato, nome="candidato"):
        confirmacao = input("Confirma o voto? (S/N): ").upper()
        while confirmacao == "N" or confirmacao != "S":
            candidato = input(
                f"Digite novamente o número do {nome} que deseja votar: ")
            confirmacao = input("Confirma o voto? (S/N): ").upper()
        return candidato
