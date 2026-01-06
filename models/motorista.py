from abc import ABC
from datetime import datetime

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
