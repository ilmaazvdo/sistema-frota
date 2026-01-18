# 🚚 Sistema de Gerenciamento de Frota - UFCA

Projeto final desenvolvido para a disciplina de **Programação Orientada a Objetos (POO)** do curso de Tecnologia em Análise e Desenvolvimento de Sistemas da **Universidade Federal do Cariri (UFCA)**.

## 👥 Equipe e Funções
* **Ilma Rodrigues V Azevedo (Tech Leader):** Responsável pela arquitetura do sistema, modelagem do domínio (`models/`), implementação de Mixins para herança múltipla, encapsulamento e métodos especiais.
* **Gyan Carlos Mateus de Oliveira:** Responsável pela camada de visualização (`view/`), menus interativos e interface CLI.
* **Jose Nataniel Gomes Pereira:** Responsável pela camada de serviços e persistência (`repository/`), regras de negócio e integração com arquivos JSON.

---

## 🏗️ Decisões de Arquitetura (POO)
A estrutura foi projetada para cumprir 100% dos critérios de exigidos:

### 1. Herança Múltipla com Mixins
Implementamos comportamentos transversais de forma modular no arquivo `models/mixins.py`:
* **AbastecivelMixin:** Gerencia histórico e registros de combustível.
* **ManutenivelMixin:** Controla entradas e saídas de manutenção.
* **Classe Caminhao:** Exemplo prático de herança múltipla, herdando de `Veiculo`, `AbastecivelMixin` e `ManutenivelMixin`.

### 2. Encapsulamento e Validação
Utilizamos decoradores `@property` e `@setter` para proteger o estado interno dos objetos:
* **Integridade:** A quilometragem de um veículo possui validação que impede valores menores que o atual (KM retrógrado).
* **Segurança:** Atributos sensíveis são protegidos para evitar manipulação direta fora das regras de negócio.

### 3. Métodos Especiais (Magic Methods)
Implementamos métodos mágicos para otimizar a manipulação dos objetos:
* `__str__`: Representação textual amigável para o usuário.
* `__eq__`: Comparação lógica baseada em identificadores únicos (Placa/CPF).
* `__lt__`: Ordenação automática da frota por quilometragem (uso de operadores de comparação).

---

## 📐 Estrutura de Pastas
```text
sistema-frota/
├── main.py              # Ponto de entrada do sistema
├── settings.json        # Configurações globais (revisão e CNH)
├── frota.json           # Banco de dados (JSON)
├── models/              # Camada de Domínio (Trabalho da Ilma)
│   ├── __init__.py      # Exportação do pacote
│   ├── veiculo.py       # Classes base e subclasses
│   ├── motorista.py     # Gestão de motoristas e CNH
│   ├── mixins.py        # Herança múltipla (Abastecer/Manutenir)
│   └── exceptions.py    # Erros customizados
├── view/                # Interface (Trabalho do Gyan)
└── repository/          # Serviços e Persistência (Trabalho do Nataniel)
