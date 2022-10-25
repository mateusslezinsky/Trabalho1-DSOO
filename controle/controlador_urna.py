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
        self.__eleitores_votaram = []

    @property
    def urna(self):
        return self.__urna

    @urna.setter
    def urna(self, urna):
        self.__urna = urna

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def homologacao(self):
        if len(self.__controlador_eleitores.eleitores) > 0 and len(self.__controlador_candidatos.candidatos) > 0:
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
            if quantidade_pro_grad > 0 and quantidade_pro_ext > 0 and quantidade_pro_pesquisa > 0:
                urna = Urna(self.__controlador_candidatos.candidatos,
                            self.__controlador_eleitores.eleitores)
            else:
                urna = None
            if urna is None:
                self.__tela_urna.imprime_mensagem(
                    "Não foi possível homologar a urna! Para isso são necessários cadastros de eleitores e candidatos.")
            elif len(urna.eleitores) > 0 and len(urna.candidatos):
                urna.homologada = True
                self.__urna = urna
                self.__tela_urna.imprime_mensagem(
                    "A urna foi homologada com sucesso. O voto pode ser realizado.")
        else:
            self.__tela_urna.imprime_mensagem(
                "Não foi possível homologar a urna! Para isso são necessários cadastros de eleitores e candidatos.")

    def votacao(self):
        if self.__urna is None:
            self.__tela_urna.imprime_mensagem(
                "Para realizar a votação é necessário que a urna esteja homologada!")
        else:

            eleitor_consultado = self.__controlador_eleitores.consulta_eleitor(
                mostrar=False)
            for eleitor in self.__eleitores_votaram:
                if eleitor_consultado == eleitor:
                    self.__tela_urna.imprime_mensagem("O eleitor já votou!")
                    break
            else:
                dados_voto = self.__tela_urna.obtem_dados_voto()
                reitor = self.consulta_dados(dados_voto["reitor"])
                pro_grad = self.consulta_dados(dados_voto["pro_grad"])
                pro_ext = self.consulta_dados(dados_voto["pro_ext"])
                pro_pesquisa = self.consulta_dados(dados_voto["pro_pesquisa"])
                if isinstance(reitor, ProReitor):
                    reitor = 99
                if isinstance(pro_grad, Reitor) or (isinstance(pro_grad, ProReitor) and pro_grad.tipo_pro_reitor != TipoProReitor.GRADUACAO.value):
                    pro_grad = 99
                if isinstance(pro_ext, Reitor) or (isinstance(pro_ext, ProReitor) and pro_ext.tipo_pro_reitor != TipoProReitor.EXTENSAO.value):
                    pro_ext = 99
                if isinstance(pro_pesquisa, Reitor) or (isinstance(pro_pesquisa, ProReitor) and pro_pesquisa.tipo_pro_reitor != TipoProReitor.PESQUISA.value):
                    pro_pesquisa = 99
                voto = Voto(reitor, pro_grad, pro_ext, pro_pesquisa,
                            eleitor_consultado.tipo_eleitor)
                self.__urna.votos.append(voto)
                self.__eleitores_votaram.append(eleitor_consultado)

    def consulta_dados(self, numero_consultado):
        nulo = 99
        if numero_consultado.strip() == "":
            return 00
        for candidato in self.__urna.candidatos:
            if candidato.numero == int(numero_consultado):
                return candidato
        else:
            return nulo
