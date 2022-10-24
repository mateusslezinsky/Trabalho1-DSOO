from limite.tela_aluno import TelaAluno
from entidade.aluno import Aluno


class ControladorAlunos:
    def __init__(self, controlador_sistema):
        self.__tela_aluno = TelaAluno(self)
        self.__alunos = []
        self.__controlador_sistema = controlador_sistema
        self.opcao_crud = 0

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def tela_aluno(self):
        return self.__tela_aluno

    def abre_tela(self):
        self.__controlador_sistema.tela_crud(
            {"cadastro": self.cadastra_aluno,
             "alterar": self.altera_aluno,
             "consultar": self.consulta_aluno,
             "excluir": self.exclui_aluno(),
             "tela": self.__tela_aluno.tela_aluno_opcoes
             })

    def checa_se_ja_existe(self, id_a_checar, lista):
        for item in lista:
            if item.numero == id_a_checar:
                return True
        else:
            return False

    def cadastra_aluno(self):
        aluno = self.__tela_aluno.cadastra_aluno()
        aluno_a_cadastrar = Aluno(
            aluno["nome"], aluno["cpf"], aluno["matricula"])
        self.__alunos.append(aluno_a_cadastrar)

    def altera_aluno(self):
        aluno_consultado = self.consulta_aluno(
            mostrar=False)
        if aluno_consultado is not None:
            dados_aluno = self.__tela_aluno.cadastra_aluno()
            lista = self.__alunos
            for aluno in lista:
                if aluno.cpf == aluno_consultado.cpf:
                    aluno.nome = dados_aluno["nome"]
                    aluno.cpf = dados_aluno["cpf"]
                    aluno.matricula = dados_aluno["matricula"]

    def consulta_aluno(self, mostrar=True):
        numero_consultado = self.tela_aluno.consulta_aluno(self)
        lista = self.__alunos
        for aluno in lista:
            if aluno.cpf == numero_consultado:
                if mostrar:
                    self.tela_aluno.imprime_dados(aluno)
                return aluno
        else:
            self.tela_aluno.imprime_dados(
                None)

    def exclui_aluno(self):
        aluno_consultado = self.consulta_aluno()
        if aluno_consultado is not None:
            lista = self.__alunos
            for aluno in lista:
                if aluno.cpf == aluno_consultado.cpf:
                    lista.remove(aluno)
                    self.__tela_aluno.exclui_aluno()
