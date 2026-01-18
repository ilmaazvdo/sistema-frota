from datetime import datetime
from models.veiculo import Veiculo, Carro, Moto, Caminhao
from models.motorista import Motorista
from models.exceptions import AlocacaoInvalidaError, FrotaError
from services.frota_repository import FrotaRepository

def serialize_obj(obj):
    """Converte objetos para formatos compatíveis com JSON."""
    data = {}
    for k, v in obj.__dict__.items():
        if isinstance(v, datetime):
            data[k] = v.isoformat()
        else:
            data[k] = v
    if hasattr(obj, "tipo"):
        data["tipo"] = obj.tipo
    return data

class FrotaService:
    def __init__(self, repo: FrotaRepository):
        self.repo = repo

    def registrar_veiculo(self, veiculo: Veiculo):
        self.repo.add("veiculos", veiculo.placa, serialize_obj(veiculo))

    def atualizar_km(self, veiculo: Veiculo, km_novo: float):
        if km_novo < veiculo.quilometragem:
            raise ValueError("Quilometragem não pode retroceder.")
        veiculo.quilometragem = km_novo
        self.repo.update("veiculos", veiculo.placa, serialize_obj(veiculo))

    def registrar_abastecimento(self, veiculo: Veiculo, litros, valor, tipo_comb):
        if not hasattr(veiculo, "abastecer"):
            raise FrotaError("Este veículo não suporta abastecimento.")
        veiculo.abastecer(litros, valor, tipo_comb)
        self.repo.update("veiculos", veiculo.placa, serialize_obj(veiculo))

    def registrar_manutencao(self, veiculo: Veiculo, tipo, custo, desc):
        if not hasattr(veiculo, "registrar_manutencao"):
            raise FrotaError("Este veículo não suporta manutenção.")
        veiculo.registrar_manutencao(tipo, custo, desc)
        self.repo.update("veiculos", veiculo.placa, serialize_obj(veiculo))

    def registrar_motorista(self, motorista: Motorista):
        self.repo.add("motoristas", motorista.cpf, serialize_obj(motorista))

    def vincular_motorista(self, motorista: Motorista, veiculo: Veiculo):
        autorizado, msg = motorista.pode_dirigir(veiculo)
        if not autorizado:
            raise AlocacaoInvalidaError(msg)
        veiculo.motorista = motorista
        self.repo.update("veiculos", veiculo.placa, serialize_obj(veiculo))
        return msg

    def gerar_relatorio(self) -> dict:
        return {
            "veiculos": self.repo.list("veiculos"),
            "motoristas": self.repo.list("motoristas"),
            "total_veiculos": len(self.repo.list("veiculos")),
            "total_motoristas": len(self.repo.list("motoristas")),
        }
