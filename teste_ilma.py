from models import Carro, Motorista

# 1. Teste de Cadastro e __str__ (Seu método especial)
c1 = Carro("ABC-1234", "Fusca", 1970, 500.0)
c2 = Carro("XYZ-9999", "Civic", 2022, 100.0)
print(f"Teste __str__: {c1}") 

# 2. Teste de Ordenação __lt__ (Sua lógica de KM)
frota = [c1, c2]
frota.sort() # Aqui o Python usa o seu __lt__
print(f"Menor KM primeiro: {frota[0].modelo} com {frota[0].quilometragem}km")

# 3. Teste de Encapsulamento (@property e setter)
try:
    c1.quilometragem = 400 # Tentar diminuir a KM
except ValueError as e:
    print(f"Sucesso! O sistema barrou a KM menor: {e}")
