from entidade.urna import Urna
from limite.tela_urna import TelaUrna
from entidade.reitor import Reitor
from entidade.pro_reitor import ProReitor, TipoProReitor
from entidade.voto import Voto


class ControladorUrna:
    def __init__(self, controlador_sistema, controlador_candidatos, controlador_eleitores) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__controlador_candidatos = controlador_candidatos
        self.__controlador_eleitores = controlador_eleitores
        self.__tela_urna = TelaUrna(self)
        self.__urna = None
        self.__votacao_encerrada = False
        self.__resultados_calculados = False
        self.__eleitores_votaram = []

    @property
    def tela_urna(self):
        return self.__tela_urna

    @property
    def urna(self):
        return self.__urna

    @urna.setter
    def urna(self, urna):
        self.__urna = urna

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def abre_tela(self):
        opcoes = {0: self.__controlador_sistema.abre_tela,
                  1: self.homologacao,
                  2: self.votacao,
                  3: self.encerra_votacao,
                  4: self.calcula_resultado}
        while True:
            try:
                opcao_escolhida = self.__tela_urna.tela_principal()
                opcoes[opcao_escolhida]()
            except (KeyError, ValueError, KeyboardInterrupt):
                self.__controlador_sistema.tela_sistema.lida_com_erro()

    def homologacao(self):
        quantidade_pro_grad = 0
        quantidade_pro_ext = 0
        quantidade_pro_pesquisa = 0
        for pro_reitor in self.__controlador_candidatos.candidatos:
            if isinstance(pro_reitor, ProReitor):
                if pro_reitor.tipo_pro_reitor == 1:
                    quantidade_pro_grad += 1
                elif pro_reitor.tipo_pro_reitor == 2:
                    quantidade_pro_ext += 1
                elif pro_reitor.tipo_pro_reitor == 3:
                    quantidade_pro_pesquisa += 1
        if len(self.__controlador_eleitores.eleitores) > 0 \
                and len(self.__controlador_candidatos.candidatos) > 0 \
                and quantidade_pro_grad > 0 \
                and quantidade_pro_ext > 0 \
                and quantidade_pro_pesquisa > 0:
            if self.__urna is None:
                urna = Urna(self.__controlador_candidatos.candidatos,
                            self.__controlador_eleitores.eleitores)
                self.__urna = urna
                self.__urna.homologada = True
                self.__votacao_encerrada = False
                self.__tela_urna.imprime_mensagem(
                    "A urna foi homologada com sucesso. O voto pode ser realizado.")
                return
            else:
                self.__tela_urna.imprime_mensagem("A urna já está homologada!")
        else:
            self.__tela_urna.imprime_mensagem(
                "Não foi possível homologar a urna! Para isso são necessários cadastros de eleitores e candidatos.")

    def consulta_dados(self, numero_consultado):
        nulo = 99
        if numero_consultado.strip() == "":
            return 00
        if numero_consultado.isdigit():
            for candidato in self.__urna.candidatos:
                if candidato.numero == int(numero_consultado):
                    return candidato
            else:
                return nulo
        return nulo

    def votacao(self):
        if self.__urna is None:
            self.__tela_urna.imprime_mensagem(
                "Para realizar a votação é necessário que a urna esteja homologada!")
        else:
            if self.__votacao_encerrada:
                self.__tela_urna.imprime_mensagem("A votação está encerrada!")
            else:
                eleitor_consultado = self.__controlador_eleitores.consulta_eleitor()
                if eleitor_consultado is not None:
                    for eleitor in self.__eleitores_votaram:
                        if eleitor_consultado == eleitor:
                            self.__tela_urna.imprime_mensagem(
                                "O eleitor já votou!")
                            break
                    else:
                        dados_voto = self.__tela_urna.obtem_dados_voto()
                        reitor = self.consulta_dados(dados_voto["reitor"])
                        pro_grad = self.consulta_dados(dados_voto["pro_grad"])
                        pro_ext = self.consulta_dados(dados_voto["pro_ext"])
                        pro_pesquisa = self.consulta_dados(
                            dados_voto["pro_pesquisa"])
                        if isinstance(reitor, ProReitor):
                            reitor = 99
                        if isinstance(pro_grad, Reitor) \
                            or (isinstance(pro_grad, ProReitor)
                                and pro_grad.tipo_pro_reitor != TipoProReitor.GRADUACAO.value):
                            pro_grad = 99
                        if isinstance(pro_ext, Reitor)\
                                or (isinstance(pro_ext, ProReitor)
                                    and pro_ext.tipo_pro_reitor != TipoProReitor.EXTENSAO.value):
                            pro_ext = 99
                        if isinstance(pro_pesquisa, Reitor) \
                            or (isinstance(pro_pesquisa, ProReitor)
                                and pro_pesquisa.tipo_pro_reitor != TipoProReitor.PESQUISA.value):
                            pro_pesquisa = 99
                        print(reitor, pro_grad, pro_ext, pro_pesquisa)
                        voto = Voto(reitor, pro_grad, pro_ext, pro_pesquisa,
                                    eleitor_consultado.tipo_eleitor)
                        self.__urna.votos.append(voto)
                        self.__eleitores_votaram.append(eleitor_consultado)

    def obtem_proporcao(self, voto):
        if voto.tipo_eleitor == 1:
            proporcao = 1/400
        elif voto.tipo_eleitor == 2:
            proporcao = 1/25
        elif voto.tipo_eleitor == 3:
            proporcao = 1/31
        return proporcao * 100

    def calcula_resultado(self):
        if self.__votacao_encerrada and self.__urna is not None:
            if self.__resultados_calculados is False:
                for voto in self.__urna.votos:
                    proporcao = self.obtem_proporcao(voto)
                    for candidato in self.__urna.candidatos:
                        if voto.reitor == candidato or \
                                voto.pro_grad == candidato or \
                                voto.pro_ext == candidato or \
                                voto.pro_pesquisa == candidato:
                            if voto.tipo_eleitor == 1:
                                candidato.votos_aluno += 1
                            elif voto.tipo_eleitor == 2:
                                candidato.votos_professor += 1
                            elif voto.tipo_eleitor == 3:
                                candidato.votos_servidor += 1
                            candidato.pontuacao += proporcao
                reitor_vencendo = None
                pro_grad_vencendo = None
                pro_ext_vencendo = None
                pro_pesquisa_vencendo = None
                for candidato in self.__urna.candidatos:
                    if isinstance(candidato, Reitor):
                        if reitor_vencendo is None or candidato.pontuacao > reitor_vencendo.pontuacao:
                            reitor_vencendo = candidato
                    if isinstance(candidato, ProReitor):
                        if candidato.tipo_pro_reitor == 1:
                            if pro_grad_vencendo is None or candidato.pontuacao > pro_grad_vencendo.pontuacao:
                                pro_grad_vencendo = candidato
                        elif candidato.tipo_pro_reitor == 2:
                            if pro_ext_vencendo is None or candidato.pontuacao > pro_ext_vencendo.pontuacao:
                                pro_ext_vencendo = candidato
                        elif candidato.tipo_pro_reitor == 3:
                            if pro_pesquisa_vencendo is None or candidato.pontuacao > pro_pesquisa_vencendo.pontuacao:
                                pro_pesquisa_vencendo = candidato
                self.__tela_urna.escreve_quantidades()
                self.__tela_urna.escreve_resultados(
                    [reitor_vencendo, pro_grad_vencendo, pro_ext_vencendo, pro_pesquisa_vencendo])
                self.__resultados_calculados = True
                self.__tela_urna.imprime_mensagem(
                    "Os resultados foram escritos para o arquivo resultados.txt.")
                self.__tela_urna.imprime_mensagem(
                    "A quantidade total de votos foi escrita para o arquivo quantidade_votos.txt.")
            else:
                self.__tela_urna.imprime_mensagem(
                    "Os resultados já foram calculados!")
        else:
            self.__tela_urna.imprime_mensagem(
                "É necessário que a votação seja encerrada primeiro!")

    def encerra_votacao(self):
        if self.__urna is not None and len(self.__urna.votos) > 0:
            if self.__votacao_encerrada:
                self.__tela_urna.imprime_mensagem(
                    "A votação já está encerrada!")
            else:
                self.__votacao_encerrada = True
                self.__tela_urna.imprime_mensagem("Votação encerrada!")
        else:
            self.__tela_urna.imprime_mensagem("Não há votos na urna!")
