import sys
import os

from models.veiculo import Carro, Moto, Caminhao, Veiculo
from models.motorista import Motorista
from models.exceptions import FrotaError
from models.servicos import FrotaRepository, FrotaService

class CLI:
    def __init__(self):
        self.frota = []
        self.motoristas = []
        # Integração com JSON
        self.repo = FrotaRepository()
        self.service = FrotaService(self.repo)

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        while True:
            print("\n=== SISTEMA DE GESTÃO DE FROTA ===")
            print("1. Cadastrar Veículo")
            print("2. Listar Frota")
            print("3. Atualizar Quilometragem")
            print("4. Registrar Abastecimento")
            print("5. Registrar Manutenção")
            print("6. Cadastrar Motorista")
            print("0. Sair")
            
            opcao = input("Escolha uma opção: ")

            try:
                if opcao == '1':
                    self.cadastrar_veiculo()
                elif opcao == '2':
                    self.listar_frota()
                elif opcao == '3':
                    self.atualizar_km()
                elif opcao == '4':
                    self.registrar_abastecimento()
                elif opcao == '5':
                    self.registrar_manutencao()
                elif opcao == '6':
                    self.cadastrar_motorista()
                elif opcao == '0':
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida!")
            except FrotaError as e:
                print(f"[ERRO DE NEGÓCIO] {e}")
            except ValueError as e:
                print(f"[ERRO DE DADOS] {e}")
            except Exception as e:
                print(f"[ERRO INESPERADO] {e}")

    def cadastrar_veiculo(self):
        print("\n--- Novo Veículo ---")
        tipo = input("Tipo (carro/moto/caminhao): ").lower()
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        ano = int(input("Ano: "))
        
        veiculo = None
        if tipo == 'carro':
            veiculo = Carro(placa, modelo, ano)
        elif tipo == 'moto':
            veiculo = Moto(placa, modelo, ano)
        elif tipo == 'caminhao':
            cap = float(input("Capacidade (ton): "))
            veiculo = Caminhao(placa, modelo, ano, cap_ton=cap)
        else:
            print("Tipo de veículo desconhecido.")
            return

        self.frota.append(veiculo)
        self.service.registrar_veiculo(veiculo)  # salva no JSON
        print(f"Veículo {modelo} ({placa}) cadastrado com sucesso!")

    def listar_frota(self):
        print("\n--- Frota Atual ---")
        relatorio = self.service.gerar_relatorio()
        if not relatorio["veiculos"]:
            print("Nenhum veículo cadastrado.")
            return
        for v in relatorio["veiculos"]:
            print(v)

    def atualizar_km(self):
        placa = input("Placa do veículo: ")
        veiculo = self._buscar_veiculo(placa)
        if veiculo:
            novo_km = float(input("Nova KM: "))
            veiculo.quilometragem = novo_km 
            self.service.registrar_veiculo(veiculo)  # atualiza no JSON
            print("Quilometragem atualizada.")
        else:
            print("Veículo não encontrado.")

    def registrar_abastecimento(self):
        placa = input("Placa do veículo: ")
        veiculo = self._buscar_veiculo(placa)
        if veiculo and hasattr(veiculo, 'abastecer'):
            litros = float(input("Litros: "))
            valor = float(input("Valor total: "))
            tipo_comb = input("Tipo Combustível: ")
            veiculo.abastecer(litros, valor, tipo_comb)
            self.service.registrar_veiculo(veiculo)  # salva histórico no JSON
        else:
            print("Veículo não encontrado ou não suporta abastecimento.")

    def registrar_manutencao(self):
        placa = input("Placa do veículo: ")
        veiculo = self._buscar_veiculo(placa)
        if veiculo and hasattr(veiculo, 'registrar_manutencao'):
            tipo = input("Tipo (preventiva/corretiva): ")
            custo = float(input("Custo: "))
            desc = input("Descrição: ")
            veiculo.registrar_manutencao(tipo, custo, desc)
            self.service.registrar_veiculo(veiculo)  # salva no JSON
            print(f"Manutenção registrada. Veículo em manutenção: {veiculo._em_manutencao}")
        elif veiculo:
            print(f"O veículo do tipo '{veiculo.tipo_veiculo}' não suporta registro de manutenção.")
        else:
            print("Veículo não encontrado.")

    def cadastrar_motorista(self):
        print("\n--- Novo Motorista ---")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        cnh = input("CNH: ")
        cat = input("Categoria: ")
        validade = input("Validade (DD/MM/AAAA): ")
        
        mt = Motorista(nome, cpf, cnh, cat, validade)
        self.motoristas.append(mt)
        self.service.registrar_motorista(mt)  # salva no JSON
        print(mt)

    def _buscar_veiculo(self, placa):
        for v in self.frota:
            if v.placa == placa:
                return v
        return None

# Bloco principal para rodar o menu
if __name__ == "__main__":
    try:
        app = CLI()
        app.menu()
    except Exception as e:
        print(f"Erro fatal ao iniciar: {e}")
        input("Pressione ENTER para sair...")
