# models/servicos.py

import json
import os
from typing import List, Optional
from datetime import datetime

from models.veiculo import Carro, Moto, Caminhao, Veiculo
from models.motorista import Motorista
from models.exceptions import AlocacaoInvalidaError, FrotaError, VeiculoIndisponivelError

FROTA_FILE = "frota.json"

def serialize_obj(obj):
    """Converte objetos para formatos compatíveis com JSON."""
    data = {}
    for k, v in obj.__dict__.items():
        if isinstance(v, datetime):
            data[k] = v.strftime("%Y-%m-%d")
        else:
            data[k] = v
    if hasattr(obj, "tipo_veiculo"):
        data["tipo_veiculo"] = obj.tipo_veiculo
    return data

class FrotaRepository:
    def __init__(self, filename: str = FROTA_FILE):
        self.filename = filename
        self._data = {"veiculos": {}, "motoristas": {}}
        self.load()

    def add(self, categoria: str, key: str, obj: dict):
        self._data[categoria][key] = obj
        self._save()

    def get_by_id(self, categoria: str, key: str) -> Optional[dict]:
        return self._data[categoria].get(key)

    def list(self, categoria: str) -> List[dict]:
        return list(self._data[categoria].values())

    def update(self, categoria: str, key: str, obj: dict):
        if key in self._data[categoria]:
            self._data[categoria][key] = obj
            self._save()

    def remove(self, categoria: str, key: str):
        if key in self._data[categoria]:
            del self._data[categoria][key]
            self._save()

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=4, ensure_ascii=False)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                try:
                    self._data = json.load(f)
                except json.JSONDecodeError:
                    self._data = {"veiculos": {}, "motoristas": {}}
        else:
            self._save()

class FrotaService:
    def __init__(self, repo: FrotaRepository):
        self.repo = repo

    def registrar_veiculo(self, veiculo: Veiculo):
        self.repo.add("veiculos", veiculo.placa, serialize_obj(veiculo))

    def registrar_motorista(self, motorista: Motorista):
        self.repo.add("motoristas", motorista.cpf, serialize_obj(motorista))

    def gerar_relatorio(self) -> dict:
        return {
            "veiculos": self.repo.list("veiculos"),
            "motoristas": self.repo.list("motoristas"),
            "total_veiculos": len(self.repo.list("veiculos")),
            "total_motoristas": len(self.repo.list("motoristas")),
        }

# Exemplo de uso automático (opcional)
if __name__ == "__main__":
    repo = FrotaRepository()
    service = FrotaService(repo)
    carro = Carro("ABC-1234", "Fusca", 1980, 1000.0)
    motorista = Motorista("João", "11122233344", "CNH1", "B", "01/01/2030")
    service.registrar_veiculo(carro)
    service.registrar_motorista(motorista)
    print("Relatório:", service.gerar_relatorio())
