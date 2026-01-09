# 🚚 Sistema de Gestão de Frota

Projeto desenvolvido para a disciplina de Programação Orientada a Objetos (POO). O sistema foca na organização, monitoramento e manutenção de uma frota de veículos e seus respectivos motoristas.

## 🏗️ Estrutura do Projeto (MVC)
O projeto utiliza a arquitetura MVC (Model-View-Controller) para garantir a separação de responsabilidades:
- **Models**: Contém a lógica de negócio, classes principais e regras de validação.
- **View**: Interface de interação com o usuário.
- **Raiz (main.py)**: Ponto de entrada que integra e executa o sistema.



## 🛠️ Tecnologias e Conceitos Aplicados
Este projeto inicial já contempla conceitos avançados de POO:
- **Classes Abstratas (ABC)**: Garantindo o polimorfismo entre tipos de veículos.
- **Mixins**: Implementação de herança múltipla para comportamentos de *Abastecimento* e *Manutenção*.
- **Tratamento de Exceções**: Criação de erros customizados para regras de negócio (ex: CNH vencida ou veículo em manutenção).
- **Encapsulamento**: Uso de `@property` e `@setter` para proteção de dados sensíveis como Placa e Quilometragem.

## 👥 Equipe
- **Ilma Azevedo** (Tech Lead)
- **Nataniel**
- **Gyan**

## 🚀 Como Executar
1. Certifique-se de ter o Python 3.x instalado.
2. Clone o repositório:
   ```bash
   git clone [https://github.com/ilmaazvdo/sistema-frota.git](https://github.com/ilmaazvdo/sistema-frota.git)