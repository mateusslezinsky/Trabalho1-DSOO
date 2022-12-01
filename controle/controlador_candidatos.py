from limite.tela_candidato import TelaCandidato
from entidade.reitor import Reitor
from entidade.pro_reitor import ProReitor, TipoProReitor


class ControladorCandidatos:
    def __init__(self, controlador_sistema, controlador_chapas):
        self.__tela_candidato = TelaCandidato(self)
        self.__candidatos = []
        self.__controlador_sistema = controlador_sistema
        self.__controlador_chapas = controlador_chapas
        self.opcao_crud = 0
        self.opcao_tipo_candidato = 0

    @property
    def candidatos(self):
        return self.__candidatos

    @candidatos.setter
    def candidatos(self, candidatos):
        self.__candidatos = candidatos

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def controlador_chapas(self):
        return self.__controlador_chapas

    @property
    def tela_candidato(self):
        return self.__tela_candidato

    def escolhe_tipo_candidato(self):
        if self.opcao_crud == 1:
            opcoes = {0: self.abre_tela,
                      1: self.cadastra_candidato,
                      2: self.cadastra_candidato}
        elif self.opcao_crud == 2:
            opcoes = {0: self.abre_tela,
                      1: self.altera_candidato,
                      2: self.altera_candidato}
        elif self.opcao_crud == 3:
            opcoes = {0: self.abre_tela,
                      1: self.consulta_candidato,
                      2: self.consulta_candidato}
        elif self.opcao_crud == 4:
            opcoes = {0: self.abre_tela,
                      1: self.exclui_candidato,
                      2: self.exclui_candidato}
        while True:
            try:
                opcao_escolhida = self.__tela_candidato.tela_escolha_cadastro()
                self.opcao_tipo_candidato = opcao_escolhida
                opcoes[opcao_escolhida]()
            except(KeyError, ValueError, KeyboardInterrupt):
                self.__controlador_sistema.tela_sistema.lida_com_erro()

    def abre_tela(self):
        self.__controlador_sistema.tela_crud(
            {"cadastro": self.escolhe_tipo_candidato,
             "alterar": self.escolhe_tipo_candidato,
             "consultar": self.escolhe_tipo_candidato,
             "excluir": self.escolhe_tipo_candidato,
             "tela": self.__tela_candidato.tela_candidato_opcoes
             })

    def checa_se_ja_existe(self, id_a_checar, lista):
        for item in lista:
            if item.numero == id_a_checar:
                return True
        else:
            return False

    def cadastra_candidato(self):
        candidato = self.__tela_candidato.cadastrar_candidato()
        if candidato is None:
            return
        elif len(candidato["nome"]) == 0:
            self.__tela_candidato.error("Nome inexistente!")
            return
        for candidato_loop in self.__candidatos:
            if candidato["numero"] == candidato_loop.numero:
                self.__tela_candidato.error("Número já cadastrado!")
                return
        cadastra_ou_nao = self.considera_segundo_turno(candidato)
        objeto_chapa = self.__controlador_chapas.consulta_chapa(
            mostrar=False)
        if objeto_chapa is not None:
            if self.opcao_tipo_candidato == 1:
                if cadastra_ou_nao:
                    self.__tela_candidato.imprime_resposta_segundo_turno()
                    return
                else:
                    reitor_a_cadastrar = Reitor(
                        candidato["nome"], candidato["numero"], objeto_chapa)
                    self.__candidatos.append(reitor_a_cadastrar)
            elif self.opcao_tipo_candidato == 2:
                if cadastra_ou_nao:
                    self.__tela_candidato.imprime_resposta_segundo_turno()
                    return
                else:
                    if candidato["tipo_pro_reitor"] == 1:
                        pro_reitor_a_cadastrar = ProReitor(
                            candidato["nome"], candidato["numero"], objeto_chapa, TipoProReitor.GRADUACAO.value)
                    elif candidato["tipo_pro_reitor"] == 2:
                        pro_reitor_a_cadastrar = ProReitor(
                            candidato["nome"], candidato["numero"], objeto_chapa, TipoProReitor.EXTENSAO.value)
                    elif candidato["tipo_pro_reitor"] == 3:
                        pro_reitor_a_cadastrar = ProReitor(
                            candidato["nome"], candidato["numero"], objeto_chapa, TipoProReitor.PESQUISA.value)
                    self.__candidatos.append(
                        pro_reitor_a_cadastrar)

    def altera_candidato(self):
        candidato_consultado = self.consulta_candidato(mostrar=False)
        if candidato_consultado is not None:
            dados_candidato = self.__tela_candidato.altera_candidato(
                candidato_consultado)
            config_segundo_turno = self.considera_segundo_turno(
                dados_candidato)
            objeto_chapa = self.controlador_chapas.consulta_chapa(
                mostrar=False)
            if objeto_chapa is not None:
                for candidato in self.__candidatos:
                    if candidato.numero == candidato_consultado.numero:
                        candidato.nome = dados_candidato["nome"]
                        candidato.numero = dados_candidato["numero"]
                        if self.opcao_tipo_candidato == 2:
                            if config_segundo_turno:
                                self.__tela_candidato.imprime_resposta_segundo_turno()
                            else:
                                candidato.tipo_pro_reitor = dados_candidato["tipo_pro_reitor"]
                        candidato.chapa = objeto_chapa

    def consulta_candidato(self, mostrar=True):
        numero_consultado = self.tela_candidato.consulta_candidato()
        if numero_consultado is None:
            return
        for candidato in self.__candidatos:
            if candidato.numero == numero_consultado:
                if mostrar:
                    self.tela_candidato.imprime_dados(
                        candidato)
                return candidato
        else:
            self.tela_candidato.imprime_dados(
                None)

    def exclui_candidato(self):
        candidato_consultado = self.consulta_candidato(mostrar=False)
        if candidato_consultado is not None:
            for candidato in self.__candidatos:
                if candidato.numero == candidato_consultado.numero:
                    self.__candidatos.remove(candidato)
                    self.__tela_candidato.remove_candidato(candidato)

    def considera_segundo_turno(self, dados_candidato):
        if self.__controlador_sistema.controlador_urna.segundo_turno:
            quantidade_reitor, quantidade_pro_grad, quantidade_pro_ext, quantidade_pro_pesquisa = self.conta_candidatos()

            if self.opcao_tipo_candidato == 1:
                if quantidade_reitor >= 2:
                    return True
            elif dados_candidato["tipo_pro_reitor"] == TipoProReitor.GRADUACAO.value:
                if quantidade_pro_grad >= 2:
                    return True
            elif dados_candidato["tipo_pro_reitor"] == TipoProReitor.EXTENSAO.value:
                if quantidade_pro_ext >= 2:
                    return True
            elif dados_candidato["tipo_pro_reitor"] == TipoProReitor.PESQUISA.value:
                if quantidade_pro_pesquisa >= 2:
                    return True
            else:
                return False
        else:
            return False

    def conta_candidatos(self):
        quantidade_reitor = 0
        quantidade_pro_grad = 0
        quantidade_pro_ext = 0
        quantidade_pro_pesquisa = 0
        for candidato in self.__candidatos:
            if isinstance(candidato, Reitor):
                quantidade_reitor += 1
            elif isinstance(candidato, ProReitor):
                if candidato.tipo_pro_reitor == TipoProReitor.GRADUACAO.value:
                    quantidade_pro_grad += 1
                elif candidato.tipo_pro_reitor == TipoProReitor.EXTENSAO.value:
                    quantidade_pro_ext += 1
                elif candidato.tipo_pro_reitor == TipoProReitor.PESQUISA.value:
                    quantidade_pro_pesquisa += 1
        return quantidade_reitor, quantidade_pro_grad, quantidade_pro_ext, quantidade_pro_pesquisa
