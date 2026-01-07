from datetime import datetime
from models.exceptions import ManutencaoInvalidaError

class AbastecivelMixin:
    def __init__(self):
        self._historico_abastecimentos = []

    def abastecer(self, litros: float, valor: float, tipo_combustivel: str):
        registro = {
            "data": datetime.now().isoformat(),
            "litros": litros,
            "valor": valor,
            "tipo": tipo_combustivel
        }
        self._historico_abastecimentos.append(registro)
        print(f"Abastecimento de {litros}L registrado.")

class ManutenivelMixin:
    def __init__(self):
        self._historico_manutencoes = []
        self._em_manutencao = False

    def registrar_manutencao(self, tipo: str, custo: float, descricao: str):
        registro = {
            "data": datetime.now().isoformat(),
            "tipo": tipo,
            "custo": custo,
            "descricao": descricao
        }
        self._historico_manutencoes.append(registro)
        self._em_manutencao = True # Muda estado [cite: 28]
    
    def finalizar_manutencao(self):
        self._em_manutencao = False

