from models.veiculo import Veiculo, Carro
from models.motorista import Motorista

def main():
    print("="*30)
    print("SISTEMA DE GESTÃO DE FROTA")
    print("="*30)

    # 1. Criando o objeto Motorista (com os 5 argumentos da sua classe)
    # Note que agora usamos 'motorista' para combinar com o print lá embaixo
    motorista = Motorista("João Silva", "123.456.789-00", "987654321", "D", "20/12/2026")
    
    # 2. Criando o objeto Carro (as outras 2 classes: Veiculo e Carro)
    carro = Carro("ABC-1234", "Corolla", 50000, 4)

    # 3. Exibindo os resultados integrados
    print(f"Sucesso! {motorista.nome} foi escalado para o {carro.modelo}.")
    print(f"Status da CNH: {motorista.cnh_valida()}") # Isso mostra a lógica que você criou!
    print("Sistema integrado com sucesso!")

if __name__ == "__main__":
    main()