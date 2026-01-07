import sys
from datetime import datetime
from veiculo import Carro, Moto, Caminhao, Veiculo
from motorista import Motorista
from mixins import ManutenivelMixin, AbastecivelMixin

# "Banco de dados" em memória
frota = []
motoristas = []

def cadastrar_veiculo():
    print("\n--- Cadastro de Veículo ---")
    tipo = input("Tipo (1-Carro, 2-Moto, 3-Caminhão): ").strip()
    placa = input("Placa: ").strip()
    modelo = input("Modelo: ").strip()
    try:
        ano = int(input("Ano: "))
        km = float(input("Quilometragem atual: "))
    except ValueError:
        print("Erro: Ano e KM devem ser números.")
        return

    veiculo = None
    if tipo == '1':
        veiculo = Carro(placa, modelo, ano, km)
    elif tipo == '2':
        veiculo = Moto(placa, modelo, ano, km)
    elif tipo == '3':
        cap = float(input("Capacidade (toneladas): "))
        veiculo = Caminhao(placa, modelo, ano, km, cap)
    else:
        print("Tipo inválido.")
        return

    frota.append(veiculo)
    print(f"Veículo {modelo} ({veiculo.tipo_veiculo}) cadastrado com sucesso!")

def cadastrar_motorista():
    print("\n--- Cadastro de Motorista ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cnh = input("Número CNH: ")
    cat = input("Categoria CNH: ")
    validade = input("Validade CNH (DD/MM/AAAA): ")
    
    # A classe Motorista já trata a validação da data no __init__
    moto = Motorista(nome, cpf, cnh, cat, validade)
    motoristas.append(moto)
    print(f"Motorista cadastrado. Status CNH: {'Válida' if moto.cnh_valida() else 'Expirada'}")

def gerenciar_frota():
    if not frota:
        print("Nenhum veículo cadastrado.")
        return

    # Demonstração do método __lt__ (ordenação por KM) definido em
    frota_ordenada = sorted(frota)
    
    print("\n--- Frota (Ordenada por Quilometragem) ---")
    for i, v in enumerate(frota_ordenada):
        print(f"{i+1}. {v}")

    idx = int(input("\nSelecione o número do veículo para ações (0 para voltar): ")) - 1
    if idx < 0 or idx >= len(frota_ordenada):
        return

    veiculo_selecionado = frota_ordenada[idx]
    
    print(f"\nAções para: {veiculo_selecionado.modelo}")
    print("1. Atualizar KM")
    print("2. Abastecer")
    print("3. Registrar Manutenção")
    
    acao = input("Escolha: ")

    if acao == '1':
        try:
            nova_km = float(input("Nova KM: "))
            # O setter da classe Veiculo valida se a KM não diminui
            veiculo_selecionado.quilometragem = nova_km 
            print("KM atualizada.")
        except ValueError as e:
            print(f"Erro de validação: {e}")

    elif acao == '2':
        # Verifica se possui o Mixin de Abastecimento
        if isinstance(veiculo_selecionado, AbastecivelMixin):
            litros = float(input("Litros: "))
            valor = float(input("Valor total: "))
            tipo_comb = input("Tipo combustível: ")
            veiculo_selecionado.abastecer(litros, valor, tipo_comb)
        else:
            print("Este veículo não suporta registro de abastecimento.")

    elif acao == '3':
        # Verifica se possui o Mixin de Manutenção.
        # Nota: Moto não possui ManutenivelMixin na implementação fornecida
        if isinstance(veiculo_selecionado, ManutenivelMixin):
            tipo = input("Tipo manutenção: ")
            custo = float(input("Custo: "))
            descr = input("Descrição: ")
            veiculo_selecionado.registrar_manutencao(tipo, custo, descr)
            print("Manutenção registrada. Veículo em manutenção.")
        else:
            print("Este tipo de veículo (ex: Moto) não possui gestão de manutenção no sistema.")

def main():
    while True:
        print("\n=== SISTEMA DE GESTÃO DE FROTA ===")
        print("1. Cadastrar Veículo")
        print("2. Cadastrar Motorista")
        print("3. Gerenciar Frota (Listar/Abastecer/Manutenção)")
        print("4. Sair")
        
        op = input("Opção: ")
        
        if op == '1': cadastrar_veiculo()
        elif op == '2': cadastrar_motorista()
        elif op == '3': gerenciar_frota()
        elif op == '4': break
        else: print("Opção inválida.")

if __name__ == "__main__":
    main()