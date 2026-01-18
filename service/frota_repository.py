import json
import os

FROTA_FILE = "frota.json"

class FrotaRepository:
    def __init__(self, filename: str = FROTA_FILE):
        self.filename = filename
        self._data = {"veiculos": {}, "motoristas": {}}
        self.load()

    def add(self, categoria: str, key: str, obj: dict):
        self._data[categoria][key] = obj
        self._save()

    def get_by_id(self, categoria: str, key: str):
        return self._data[categoria].get(key)

    def list(self, categoria: str):
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
