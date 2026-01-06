# 🚗 UFCA - POO: Sistema de Gerenciamento de Frota de Veículos

## Status do Projeto

| Entrega | Foco Principal | Status | Branch de Trabalho |
| :--- | :--- | :--- | :--- |
| **Entrega 1** | Modelagem de Classes e Regras | **CONCLUÍDA** | `main` |
| **Entrega 2** | Implementação do Domínio (Classes e Mixins) | **EM ANDAMENTO** | `main` |

---

## 👥 Membros da Equipe

| Membro | Matrícula | Foco Principal |
| :--- | :--- | :--- |
| Ilma Rodrigues Vieira Azevedo | 2025015455 | Tech Lead - Domínio Core e POO Avançado |
| José Nataniel Gomes Pereira | 2025015698 | Serviços, Regras de Negócio e Persistência |
| Gyan Carlos Mateus de Oliveira | 2025015339 | Mixins, Exceções e Interface CLI |

---

## 🛠️ Progresso da Entrega 2

A arquitetura do sistema foi refatorada para um modelo de pacotes profissional:

- **Pacote `models/`**: Centraliza a lógica de negócio.
- **Abstração e Herança**: Implementação de classes abstratas (ABC) e herança múltipla com Mixins.
- **Encapsulamento**: Uso de `@property` e setters para validação de dados (ex: quilometragem).
- **Métodos Especiais**: Implementação de `__str__`, `__eq__` (comparação de placas) e `__lt__` (ordenação por KM).

## 📑 Documentação de Referência

* **[MODELAGEM_ENTREGA1.md](MODELAGEM_ENTREGA1.md)** - Planejamento inicial e Diagrama de Classes.
