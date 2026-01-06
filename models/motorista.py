from abc import ABC
from datetime import datetime

class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

class Motorista(Pessoa):
    def __init__(self, nome: str, cpf: str, cnh: str, categoria_cnh: str, validade_cnh: str):
        # Integração com a classe base do Gyan
        super().__init__(nome, cpf)
        self.cnh = cnh
        self.categoria_cnh = categoria_cnh
        
        # Sua lógica de data (Ilma)
        try:
            self.validade_cnh = datetime.strptime(validade_cnh, "%d/%m/%Y")
        except ValueError:
            self.validade_cnh = datetime.now() 

    def cnh_valida(self):
        """Verifica se a CNH está dentro do prazo de validade"""
        return self.validade_cnh > datetime.now()

    def __repr__(self):
        status = "VÁLIDA" if self.cnh_valida() else "EXPIRADA"
        return f"Motorista({self.nome}, CNH: {self.categoria_cnh}, Status: {status})"
