from abc import ABC
from .mixins import AbastecivelMixin, ManutenivelMixin

class Veiculo(ABC):
    def __init__(self, placa, modelo, km_atual, consumo_medio):
        self._placa = placa  # Encapsulamento (Privado)
        self._quilometragem = km_atual
        self.modelo = modelo
        self.consumo_medio = consumo_medio
        self._status = "ATIVO"

    @property
    def quilometragem(self):
        return self._quilometragem

    @quilometragem.setter
    def quilometragem(self, valor):
        if valor < self._quilometragem:
            raise ValueError("A quilometragem não pode retroceder.")
        self._quilometragem = valor

    # Métodos Especiais Requeridos
    def __eq__(self, outro):
        return self._placa == outro._placa

    def __lt__(self, outro):
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
