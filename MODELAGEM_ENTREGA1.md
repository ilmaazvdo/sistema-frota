# 📑 UFCA - POO: Documentação da Modelagem e Plano de Implementação

## ENTREGA 1: Levantamento de Classes, Regras e Divisão de Tarefas

Este documento formaliza a arquitetura e o planejamento para a implementação do Sistema de Gerenciamento de Frota de Veículos, seguindo os princípios de Programação Orientada a Objetos.

### 1. Modelagem de Classes e Aplicação de POO

A arquitetura utiliza Herança, Mixins e Encapsulamento.

#### 1.1. Classes de Domínio e Herança Simples

| Classe | Herança | Atributos Chave (Privados) | Responsabilidades Chave (POO) |
| :--- | :--- | :--- | :--- |
| **`Veiculo`** | Base | `__placa`, `__quilometragem`, `__status` (VeiculoStatus). | **Encapsulamento** (`@property`). Implementação de **`__eq__`** (placa) e **`__lt__`** (KM). |
| **`Carro`**, **`Moto`**, **`Caminhao`** | Herdam de `Veiculo` | *N/A (Tipo de Veículo)* | Definir o tipo para **Validação CNH**. |
| **`Motorista`** | Herda de `Pessoa` | `__cnh_categoria`, `__tempo_experiencia`. | Implementar a **Validação de Compatibilidade CNH**. |

#### 1.2. Mixins (Herança Múltipla)

| Classe | Tipo | Responsabilidades Chave (Comportamentos Reutilizáveis) |
| :--- | :--- | :--- |
| **`AbastecivelMixin`** | Mixin | Adicionar método `abastecer()`. Calcular o consumo médio ($km/l$). |
| **`ManutenivelMixin`**| Mixin | Adicionar `registrar_manutencao()`. Controlar o **status** (transição para MANUTENCAO e retorno). Implementar **`__iter__`** sobre o histórico. |

#### 1.3. Camadas de Serviço, Persistência e Configuração

| Classe | Propósito | Padrões/Responsabilidades |
| :--- | :--- | :--- |
| **`FrotaService`** | Camada de Serviço | Orquestrar a Alocação, aplicando as **Regras de Negócio**. Gerar **Relatórios**. |
| **`Repository`** | Padrão Abstrato | Definir a interface CRUD (`add`, `get_by_id`, `list`, `update`, `remove`). |
| **`VeiculoStatus`** | Enum | Gerenciar os estados válidos (ATIVO, MANUTENCAO, INATIVO). |

### 2. Diagrama de Classes Conceitual

Este diagrama UML ilustra as relações de Herança e a aplicação dos Mixins.


### 3. Especificação Formal das Regras de Negócio e Interfaces

| Regra/Interface | Definição Formal | Tratamento de Erro |
| :--- | :--- | :--- |
| **Validação CNH** | CNH compatível com o tipo de veículo. Mapeamento formalizado. | Exceção customizada: `CNHIncompativelError` |
| **Bloqueio de Alocação**| Veículo deve ter status **ATIVO** para ser alocado. | Exceção customizada: `VeiculoIndisponivelError` |
| **Interface `alocar_veiculo`**| `FrotaService.alocar_veiculo(placa: str, cpf: str, destino: str) -> Viagem` | Garante a tipagem e o retorno da entidade Viagem. |
### 4. Plano de Testes Unitários

| Área de Teste | Caso de Teste Essencial | Responsável |
| :--- | :--- | :--- |
| **Regras** | Alocação de Motorista B (Carro) para um Caminhão (CNH C/D/E). | José Nataniel |
| **POO** | Ordenação de veículos por quilometragem (`sorted()` funciona). | Ilma Rodrigues |
| **Persistência** | Teste de CRUD (salvar/carregar) para garantir a integridade do JSON. | José Nataniel |
| **Interface** | Teste de comandos básicos da CLI e validação de entrada. | Gyan Carlos |

### 5. Divisão de Responsabilidades da Equipe (3 Membros)

| Membro | Matrícula | Foco Principal | Tarefas Específicas (Entrega 2) |
| :--- | :--- | :--- | :--- |
| **Ilma Rodrigues Vieira Azevedo** | 2025015455 | **Tech Lead / Domínio Core** | Implementação das Classes Base (`Veiculo`, `Motorista`, `Pessoa`). Implementação dos **Mixins** e **Métodos Especiais**. |
| **José Nataniel Gomes Pereira** | 2025015698 | **Serviços, Regras de Negócio e Persistência** | Implementação de **`FrotaService`** e **Regras de Negócio**. Implementação do **Repository** e `settings.json`. |
| **Gyan Carlos Mateus de Oliveira**| 2025015339 | **Interface CLI e Testes Unitários** | Desenvolvimento da Interface de **Linha de Comando (CLI)**. Criação e execução dos **Testes Unitários** para todas as camadas. |
