from entidade.reitor import Reitor
from entidade.pro_reitor import ProReitor, TipoProReitor


class TelaUrna:
    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna

    def tela_principal(self):
        print("\n")
        print("-"*10, "Urna", "-"*10)
        print("1 - Homologação de urna")
        print("2 - Votar")
        print("3 - Encerrar votação")
        print("4 - Resultados")
        print("0 - Voltar")
        opcao = int(input("\nEscolha sua opção: "))
        return opcao

    def imprime_mensagem(self, mensagem):
        print(mensagem)

    def obtem_dados_voto(self):
        reitor = input(
            "\nDigite o número do reitor que deseja votar: ")
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

    """ def desfaz_homologacao(self):
        homologacao = input(
            "A urna já está homologada. Deseja desfazer (S/N)? ").upper()
        if homologacao == "N" or homologacao != "S":
            return False
        return True """

    def escreve_resultados(self, candidatos):
        with open("resultados.txt", "w") as file:
            for candidato in candidatos:
                tipo_candidato = self.verifica_tipo_candidato(candidato)
                file.write(f"O {tipo_candidato} vencedor é: \n")

                file.write(f"Nome: {candidato.nome} \n")
                file.write(f"Número: {candidato.numero} \n")
                file.write(f"Pontuação: {candidato.pontuacao}\n")
                file.write(
                    f"Quantidade de votos de aluno: {candidato.votos_aluno}\n")
                file.write(
                    f"Quantidade de votos de professor: {candidato.votos_professor}\n")
                file.write(
                    f"Quantidade de votos de servidor: {candidato.votos_servidor}\n")
                file.write("-"*20)
                file.write("\n")
                file.write(f"Nome da chapa: {candidato.chapa.nome}\n")
                file.write(f"ID da chapa: {candidato.chapa.id}\n")
                file.write("-"*20)
                file.write("\n\n")

    def escreve_quantidades(self):
        with open("quantidade_votos.txt", "w") as file:
            for candidato in self.__controlador_urna.urna.candidatos:
                tipo_candidato = self.verifica_tipo_candidato(candidato)
                file.write(f"O candidato a {tipo_candidato}\n")
                file.write(f"De nome: {candidato.nome}\n")
                file.write(f"De número: {candidato.numero}\n")
                file.write(
                    f"Concorrendo pela chapa de nome: {candidato.chapa.nome}\n")
                file.write(f"Com ID de chapa: {candidato.chapa.id}\n\n")
                file.write(
                    f"Teve um total de {candidato.votos_aluno} voto(s) de aluno\n")
                file.write(
                    f"Um total de {candidato.votos_professor} voto(s) de professor\n")
                file.write(
                    f"E um total de {candidato.votos_servidor} voto(s) de servidor\n")
                file.write("-"*20)
                file.write("\n\n")

    def verifica_tipo_candidato(self, candidato):
        if isinstance(candidato, Reitor):
            return "reitor"
        if isinstance(candidato, ProReitor):
            if candidato.tipo_pro_reitor == TipoProReitor.GRADUACAO.value:
                return "pró-reitor de graduação"
            elif candidato.tipo_pro_reitor == TipoProReitor.EXTENSAO.value:
                return "pró-reitor de extensão"
            elif candidato.tipo_pro_reitor == TipoProReitor.PESQUISA.value:
                return "pró-reitor de pesquisa"
