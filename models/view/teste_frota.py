import unittest
from datetime import datetime, timedelta
from veiculo import Carro, Moto, Veiculo
from motorista import Motorista
from mixins import ManutenivelMixin

class TestMotorista(unittest.TestCase):
    def test_cnh_valida(self):
        """Testa se a validação da data da CNH funciona corretamente"""
        # Data futura (Válida)
        data_futura = (datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y")
        m1 = Motorista("João", "123", "CNH1", "B", data_futura)
        self.assertTrue(m1.cnh_valida(), "CNH com data futura deveria ser válida")

    def test_cnh_vencida(self):
        """Testa se a CNH vencida retorna False"""
        # Data passada (Vencida)
        data_passada = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y")
        m2 = Motorista("Maria", "456", "CNH2", "A", data_passada)
        self.assertFalse(m2.cnh_valida(), "CNH com data passada deveria ser inválida")

class TestVeiculo(unittest.TestCase):
    def test_encapsulamento_quilometragem(self):
        """Testa a regra de negócio onde a KM não pode retroceder"""
        carro = Carro("ABC-1234", "Fusca", 1980, 1000.0)
        
        # Tentativa válida (aumentar)
        carro.quilometragem = 1100.0
        self.assertEqual(carro.quilometragem, 1100.0)
        
        # Tentativa inválida (diminuir) - Deve lançar ValueError
        with self.assertRaises(ValueError):
            carro.quilometragem = 900.0

    def test_comparacao_veiculos(self):
        """Testa a ordenação (__lt__) e igualdade (__eq__)"""
        v1 = Carro("AAA-1111", "Modelo A", 2020, 500.0) # Menor KM
        v2 = Moto("BBB-2222", "Modelo B", 2021, 1000.0) # Maior KM
        v3 = Carro("AAA-1111", "Clone A", 2022, 0.0)    # Mesma placa que v1

        # Teste de ordenação (__lt__)
        self.assertTrue(v1 < v2, "Veículo com menor KM deve ser 'menor' que o de maior KM")
        
        # Teste de igualdade (__eq__) - Baseado na placa
        self.assertEqual(v1, v3, "Veículos com mesma placa devem ser considerados iguais")

class TestMixins(unittest.TestCase):
    def test_manutencao_estado(self):
        """Testa se registrar manutenção altera o estado interno"""
        carro = Carro("TEST-001", "Teste", 2023)
        
        # Estado inicial (acesso direto ao atributo protegido para teste)
        self.assertFalse(carro._em_manutencao)
        
        # Ação
        carro.registrar_manutencao("Troca de Óleo", 150.0, "Óleo 5w30")
        
        # Verificação: deve estar em manutenção
        self.assertTrue(carro._em_manutencao)

    def test_moto_sem_manutencao(self):
        """Garante que Moto NÃO herda de ManutenivelMixin conforme definido"""
        moto = Moto("MOTO-001", "Honda", 2022)
        self.assertNotIsInstance(moto, ManutenivelMixin, "Moto não deve herdar Mixin de Manutenção")

if __name__ == '__main__':
    unittest.main()