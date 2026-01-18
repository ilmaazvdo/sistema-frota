"""
Módulo de Exceções Customizadas - Camada de Domínio
Desenvolvido por: Ilma Rodrigues V Azevedo (Tech Leader)
"""

class FrotaError(Exception):
    """Classe base para todas as exceções do sistema de frota."""
    pass

class ManutencaoInvalidaError(FrotaError):
    """Lançada quando uma operação de manutenção viola as regras de negócio."""
    pass

class AlocacaoInvalidaError(FrotaError):
    """Lançada quando um motorista não pode ser alocado a um veículo (ex: CNH incompatível)."""
    pass

class PoliticaNaoAtendidaError(FrotaError):
    """Lançada quando uma política de uso (ex: limite de KM para revisão) não é atendida."""
    pass

class VeiculoIndisponivelError(FrotaError):
    """Lançada quando o veículo está em manutenção ou inativo e tentam utilizá-lo."""
    pass

class MotoristaInvalidoError(FrotaError):
    """Lançada quando os dados do motorista não atendem aos requisitos do sistema."""
    pass

class VeiculoNaoEncontradoError(FrotaError):
    """Lançada quando uma busca por placa não retorna resultados."""
    pass

class MotoristaNaoEncontradoError(FrotaError):
    """Lançada quando uma busca por CPF não retorna resultados."""
    pass
