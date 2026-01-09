from models.veiculo import Veiculo, Carro
from models.motorista import Motorista

def main():
    print("="*30)
    print("SISTEMA DE GESTÃO DE FROTA")
    print("="*30)

    # Criando os objetos para a entrega (3 classes)
    motorista = Motorista("João Silva", "123456", "D")
    carro = Carro("ABC-1234", "Corolla", 50000, 4)

    print(f"Sucesso! {motorista.nome} foi escalado para o {carro.modelo}.")
    print("Sistema integrado com sucesso!")

if __name__ == "__main__":
    main()