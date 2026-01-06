from abc import ABC
# O ponto '.' indica que o mixins está na mesma pasta (models)
from .mixins import AbastecivelMixin, ManutenivelMixin

class Veiculo(ABC):
    def __init__(self, placa, modelo, km_atual, consumo_medio):
        self._placa = placa  # Atributo privado conforme plano
        self._quilometragem = km_atual # Atributo privado conforme plano
        self.modelo = modelo
        self.consumo_medio = consumo_medio
        self._status = "ATIVO"

    @property
    def quilometragem(self):
        """Encapsulamento solicitado na Entrega 1"""
        return self._quilometragem

    @quilometragem.setter
    def quilometragem(self, valor):
        """Regra de negócio: impede redução de KM"""
        if valor < self._quilometragem:
            raise ValueError("A quilometragem não pode retroceder.")
        self._quilometragem = valor

    # Métodos Especiais (Requisito da Entrega 2)
    def __eq__(self, outro):
        return self._placa == outro._placa

    def __lt__(self, outro):
        """Ordenação por quilometragem (Planejado por Ilma)"""
        return self._quilometragem < outro._quilometragem

    def __str__(self):
        return f"{self.modelo} ({self._placa})"

class Carro(Veiculo, AbastecivelMixin):
    def __init__(self, placa, modelo, km_atual, consumo_medio):
        Veiculo.__init__(self, placa, modelo, km_atual, consumo_medio)
        AbastecivelMixin.__init__(self)

class Caminhao(Veiculo, AbastecivelMixin, ManutenivelMixin):
    def __init__(self, placa, modelo, km_atual, consumo_medio, cap_ton):
        Veiculo.__init__(self, placa, modelo, km_atual, consumo_medio)
        AbastecivelMixin.__init__(self)
        ManutenivelMixin.__init__(self)
        self.capacidade_toneladas = cap_ton
