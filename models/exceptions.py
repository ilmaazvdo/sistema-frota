class FrotaError(Exception):
    """Exceção base para erros do sistema de frota."""
    pass

class ManutencaoInvalidaError(FrotaError):
    """Erro quando uma manutenção é registrada de forma inválida."""
    pass

class AlocacaoInvalidaError(FrotaError):
    """Erro quando a alocação de motorista/veículo não atende às regras de negócio."""
    pass

class PoliticaNaoAtendidaError(FrotaError):
    """Erro quando alguma política de negócio não é atendida."""
    pass

class VeiculoIndisponivelError(FrotaError):
    """Erro quando o veículo não está disponível para alocação (inativo ou em manutenção)."""
    pass
