# Guia de Execução dos Testes (Pasta View)

Como os testes foram movidos para a pasta `view`, a estrutura do projeto deve estar assim:

## Estrutura de Pastas
/ (Raiz do projeto)
│── veiculo.py
│── motorista.py
│── mixins.py
│── exceptions.py
│── __init__.py
│── main.py
│
└── view/
    └── test_frota.py  <-- Arquivo movido

## Como Executar

Abra o terminal na **Raiz do projeto** (onde estão os arquivos veiculo.py, etc) e use um dos comandos abaixo:

### Opção A (Windows)
```bash
python view\test_frota.py

opção B (Mac/linux)

python3 view/test_frota.py
