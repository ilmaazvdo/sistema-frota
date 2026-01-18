import abc
from .mixins import AbastecivelMixin, ManutenivelMixin

class Veiculo(abc.ABC):
    def __init__(self, placa, marca, modelo, ano, km, consumo, tipo):
        self._placa = placa
        self._quilometragem = km
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.consumo_medio = consumo
        self.tipo = tipo
        self.status = "ATIVO"

    @property
    def placa(self): return self._placa

    @property
    def quilometragem(self): return self._quilometragem

    @quilometragem.setter
    def quilometragem(self, valor):
        if valor < self._quilometragem:
            raise ValueError("KM não pode retroceder!")
        self._quilometragem = valor

    def __str__(self): return f"{self.modelo} [{self._placa}]"
    def __eq__(self, outro): return self._placa == outro.placa
    def __lt__(self, outro): return self._quilometragem < outro.quilometragem
    def __repr__(self): return f"Veiculo(placa='{self._placa}')"

class Carro(Veiculo, AbastecivelMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        AbastecivelMixin.__init__(self)

class Moto(Veiculo, AbastecivelMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        AbastecivelMixin.__init__(self)

class Caminhao(Veiculo, AbastecivelMixin, ManutenivelMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        AbastecivelMixin.__init__(self)
        ManutenivelMixin.__init__(self)
