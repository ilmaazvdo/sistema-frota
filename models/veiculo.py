from abc import ABC, abstractmethod
from .mixins import AbastecivelMixin, ManutenivelMixin

class Veiculo(ABC):
    def __init__(self, placa: str, modelo: str, ano: int, quilometragem: float = 0.0):
        self._placa = placa  # Encapsulamento: Atributo Protegido
        self.modelo = modelo
        self.ano = ano
        self._quilometragem = quilometragem 

    # --- ENCAPSULAMENTO (REQUISITO ENTREGA 2) ---
    @property
    def placa(self):
        return self._placa

    @property
    def quilometragem(self):
        return self._quilometragem

    @quilometragem.setter
    def quilometragem(self, valor):
        # Regra de negócio: quilometragem nunca diminui
        if valor < self._quilometragem:
            raise ValueError("Erro: A quilometragem não pode retroceder.")
        self._quilometragem = valor

    @property
    @abstractmethod
    def tipo_veiculo(self) -> str:
        """Método abstrato para garantir polimorfismo nas subclasses"""
        pass

    # --- MÉTODOS ESPECIAIS (REQUISITO ENTREGA 2) ---
    
    def __str__(self):
        """Representação em string para o usuário (CLI)"""
        return f"[{self.tipo_veiculo.upper()}] {self.modelo} | Placa: {self.placa} | KM: {self.quilometragem}"

    def __eq__(self, outro):
        """Compara veículos pela placa (usado em buscas e remoções)"""
        if not isinstance(outro, Veiculo):
            return False
        return self.placa == outro.placa

    def __lt__(self, outro):
        """Permite ordenar a frota por quilometragem (do menor para o maior)"""
        return self.quilometragem < outro.quilometragem

# --- SUBCLASSES COM HERANÇA MÚLTIPLA ---

class Carro(Veiculo, AbastecivelMixin, ManutenivelMixin):
    def __init__(self, placa, modelo, ano, quilometragem=0.0):
        Veiculo.__init__(self, placa, modelo, ano, quilometragem)
        AbastecivelMixin.__init__(self)
        ManutenivelMixin.__init__(self)

    @property
    def tipo_veiculo(self):
        return "carro"

class Moto(Veiculo, AbastecivelMixin):
    def __init__(self, placa, modelo, ano, quilometragem=0.0):
        Veiculo.__init__(self, placa, modelo, ano, quilometragem)
        AbastecivelMixin.__init__(self)

    @property
    def tipo_veiculo(self):
        return "moto"

class Caminhao(Veiculo, AbastecivelMixin, ManutenivelMixin):
    def __init__(self, placa, modelo, ano, quilometragem=0.0, cap_ton=10):
        Veiculo.__init__(self, placa, modelo, ano, quilometragem)
        AbastecivelMixin.__init__(self)
        ManutenivelMixin.__init__(self)
        self.cap_ton = cap_ton

    @property
    def tipo_veiculo(self):
        return "caminhao"
