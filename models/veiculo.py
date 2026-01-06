from abc import ABC, abstractmethod
# Note o ponto '.' antes de mixins e exceptions (importante!)
from .mixins import AbastecivelMixin, ManutenivelMixin
from .exceptions import AlocacaoInvalidaError

class Veiculo(ABC):
    def __init__(self, placa: str, modelo: str, ano: int, quilometragem: float = 0.0):
        self._placa = placa
        self.modelo = modelo
        self.ano = ano
        self._quilometragem = quilometragem 

    @property
    def placa(self):
        return self._placa

    @property
    def quilometragem(self):
        return self._quilometragem

    @quilometragem.setter
    def quilometragem(self, valor):
        if valor < self._quilometragem:
            raise ValueError("Quilometragem não pode ser reduzida.")
        self._quilometragem = valor

    @property
    @abstractmethod
    def tipo_veiculo(self) -> str:
        pass

    def __str__(self):
        return f"[{self.tipo_veiculo.upper()}] {self.modelo} - Placa: {self.placa} - Km: {self.quilometragem}"

    def __eq__(self, other):
        return self.placa == other.placa

    def __lt__(self, other):
        return self.quilometragem < other.quilometragem

class Carro(Veiculo, AbastecivelMixin, ManutenivelMixin):
    def __init__(self, placa, modelo, ano, quilometragem=0.0):
        Veiculo.__init__(self, placa, modelo, ano, quilometragem)
        AbastecivelMixin.__init__(self)
        ManutenivelMixin.__init__(self)

    @property
    def tipo_veiculo(self):
        return "carro"
    
    def __iter__(self):
        return iter(self._historico_manutencoes)

class Moto(Veiculo, AbastecivelMixin, ManutenivelMixin):
    def __init__(self, placa, modelo, ano, quilometragem=0.0):
        Veiculo.__init__(self, placa, modelo, ano, quilometragem)
        AbastecivelMixin.__init__(self)
        ManutenivelMixin.__init__(self)

    @property
    def tipo_veiculo(self):
        return "moto"

class Caminhao(Veiculo, AbastecivelMixin, ManutenivelMixin):
    def __init__(self, placa, modelo, ano, quilometragem=0.0):
        Veiculo.__init__(self, placa, modelo, ano, quilometragem)
        AbastecivelMixin.__init__(self)
        ManutenivelMixin.__init__(self)

    @property
    def tipo_veiculo(self):
        return "caminhao"
