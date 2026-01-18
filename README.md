# 🚚 Sistema de Gerenciamento de Frota - UFCA

Projeto final desenvolvido para a disciplina de **Programação Orientada a Objetos (POO)** do curso de Tecnologia em Análise e Desenvolvimento de Sistemas da **Universidade Federal do Cariri (UFCA)**.

## 👥 Equipe e Funções
* **Ilma Rodrigues V Azevedo (Tech Leader & Participante 1):** Responsável pela arquitetura do sistema, modelagem do domínio (`models/`), implementação de Mixins para herança múltipla, encapsulamento e métodos especiais.
* **Gyan Carlos Mateus de Oliveira (Participante 2):** Responsável pela camada de visualização (`view/`), menus interativos e interface CLI.
* **Jose Nataniel Gomes Pereira (Participante 3):** Responsável pela camada de serviços e persistência (`repository/`), regras de negócio e integração com arquivos JSON.

---

## 🏗️ Decisões de Arquitetura (POO)
Como Tech Leader, a estrutura foi projetada para cumprir 100% dos critérios de aceite da UFCA:

### 1. Herança Múltipla com Mixins
Implementamos comportamentos transversais que não pertencem exclusivamente a uma classe pai, mas que podem ser "misturados" conforme a necessidade:
* **AbastecivelMixin:** Gerencia histórico e registros de combustível.
* **ManutenivelMixin:** Controla entradas e saídas de manutenção.
* **Classe Caminhao:** Exemplo prático de herança múltipla, herdando de `Veiculo`, `AbastecivelMixin` e `ManutenivelMixin`.

### 2. Encapsulamento e Validação
Utilizamos decoradores `@property` para proteger o estado interno dos objetos. 
- Exemplo: A quilometragem de um veículo possui um `setter` que impede que o valor seja alterado para um número menor que o atual, garantindo a integridade dos dados da frota.

### 3. Métodos Especiais (Magic Methods)
Implementamos 4+ métodos mágicos para tornar os objetos "cidadãos de primeira classe" no Python:
* `__str__`: Representação textual para o usuário.
* `__repr__`: Representação técnica para logs.
* `__eq__`: Comparação lógica por identificadores únicos (Placa/CPF).
* `__lt__`: Ordenação automática da frota por quilometragem.

---

## 📐 Estrutura de Pastas
```text
sistema-frota/
├── main.py              # Inicialização do sistema
├── settings.json        # Configurações de revisão (10.000km) e CNH
├── frota.json           # Persistência de dados
├── models/              # Domínio (Trabalho da Ilma)
│   ├── veiculo.py       # Classes base, subclasses e Mixins
│   └── motorista.py     # Classe Motorista e validações
├── view/                # Interface (Trabalho do Gyan)
└── repository/          # Persistência (Trabalho do Nataniel)
