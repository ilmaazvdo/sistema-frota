from datetime import datetime

class Motorista:
    def __init__(self, nome, cnh, categoria, validade_cnh):
        self.nome = nome
        self.cnh = cnh
        self.categoria = categoria
        self.validade_cnh = datetime.strptime(validade_cnh, "%d/%m/%Y")

    def cnh_valida(self):
        return self.validade_cnh > datetime.now()
