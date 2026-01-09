import unittest
import sys
import os
from datetime import datetime, timedelta
from models.veiculo import Carro, Moto, Caminhao
from models.motorista import Motorista


class TestFrota(unittest.TestCase):

    def setUp(self):
        """Executado antes de cada teste"""
        self.carro = Carro("ABC-1234", "Fusca", 1980, 1000.0)
        self.moto = Moto("XYZ-9876", "CB 500", 2020, 500.0)

    def test_encapsulamento_km(self):
        """Testa se a regra de não retroceder KM está funcionando"""
        # Tenta diminuir a KM (deve falhar)
        with self.assertRaises(ValueError):
            self.carro.quilometragem = 900.0
        
        # Tenta aumentar a KM (deve passar)
        self.carro.quilometragem = 1100.0
        self.assertEqual(self.carro.quilometragem, 1100.0)

    def test_mixin_abastecimento(self):
        """Testa o registro de abastecimento no histórico"""
        self.carro.abastecer(30, 150.0, "Gasolina")
        historico = self.carro._historico_abastecimentos
        
        self.assertEqual(len(historico), 1)
        self.assertEqual(historico[0]['litros'], 30)
        self.assertEqual(historico[0]['valor'], 150.0)

    def test_mixin_manutencao(self):
        """Testa registro de manutenção e mudança de estado"""
        # Carro deve ter mixin de manutenção
        self.assertTrue(hasattr(self.carro, 'registrar_manutencao'))
        
        self.carro.registrar_manutencao("Troca de Óleo", 200.0, "Óleo sintético")
        
        # Verifica se o estado mudou para em_manutencao = True
        self.assertTrue(self.carro._em_manutencao)
        self.assertEqual(len(self.carro._historico_manutencoes), 1)

    def test_moto_sem_manutencao(self):
        """Garante que Moto NÃO tem mixin de manutenção"""
        self.assertFalse(hasattr(self.moto, 'registrar_manutencao'))

    def test_validade_cnh(self):
        """Testa a validação da data da CNH"""
        data_futura = (datetime.now() + timedelta(days=365)).strftime("%d/%m/%Y")
        data_passada = (datetime.now() - timedelta(days=365)).strftime("%d/%m/%Y")

        motorista_valido = Motorista("João", "123", "CNH1", "B", data_futura)
        motorista_vencido = Motorista("José", "456", "CNH2", "B", data_passada)

        self.assertTrue(motorista_valido.cnh_valida())
        self.assertFalse(motorista_vencido.cnh_valida())

    def test_polimorfismo_str(self):
        """Testa se a representação em string identifica o tipo corretamente"""
        self.assertIn("[CARRO]", str(self.carro))
        self.assertIn("[MOTO]", str(self.moto))

if __name__ == '__main__':
    unittest.main()