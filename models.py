from abc import ABC, abstractmethod
from mixins import AbastecivelMixin, ManutenivelMixin
from config import Config
from exceptions import AlocacaoInvalidaError

class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

class Motorista(Pessoa):
    def __init__(self, nome: str, cpf: str, cnh: str, categoria_cnh: str):
        super().__init__(nome, cpf)
        self.cnh = cnh
        self.categoria_cnh = categoria_cnh

    def __repr__(self):
        return f"Motorista({self.nome}, CNH: {self.categoria_cnh})"

class Veiculo(ABC):
    def __init__(self, placa: str, modelo: str, ano: int, quilometragem: float = 0.0):
        self._placa = placa
        self.modelo = modelo
        self.ano = ano
        self._quilometragem = quilometragem # Atributo protegido

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

    # Métodos Especiais [cite: 66, 67, 68]
    def __str__(self):
        return f"[{self.tipo_veiculo.upper()}] {self.modelo} - Placa: {self.placa} - Km: {self.quilometragem}"

    def __eq__(self, other):
        return self.placa == other.placa

    def __lt__(self, other):
        return self.quilometragem < other.quilometragem

# Herança Múltipla: Herda de Veiculo e dos Mixins 
class Carro(Veiculo, AbastecivelMixin, ManutenivelMixin):
    def __init__(self, placa, modelo, ano, quilometragem=0.0):
        Veiculo.__init__(self, placa, modelo, ano, quilometragem)
        AbastecivelMixin.__init__(self)
        ManutenivelMixin.__init__(self)

    @property
    def tipo_veiculo(self):
        return "carro"
    
    # Implementação de __iter__ para histórico de manutenções [cite: 69]
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