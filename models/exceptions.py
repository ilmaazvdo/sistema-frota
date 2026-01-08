class FrotaError(Exception):
    """Erro genérico da frota"""
    pass

class ManutencaoInvalidaError(FrotaError):
    """Erro para manutenção inválida"""
    pass

class AlocacaoInvalidaError(FrotaError):
    """Erro para alocação inválida de veículo/motorista"""
    pass

class PoliticaNaoAtendidaError(FrotaError):
    """Erro quando alguma política de uso não é atendida"""
    pass

class VeiculoIndisponivelError(FrotaError):
    """Erro quando o veículo não pode ser usado (ex: em manutenção)"""
    pass

class MotoristaInvalidoError(FrotaError):
    """Erro quando o motorista não atende aos requisitos"""
    pass

class VeiculoNaoEncontradoError(FrotaError):
    """Erro quando o veículo não é encontrado no sistema"""
    pass

class MotoristaNaoEncontradoError(FrotaError):
    """Erro quando o motorista não é encontrado no sistema"""
    pass
