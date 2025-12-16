class FrotaError(Exception):
    pass

class ManutencaoInvalidaError(FrotaError):
    pass

class AlocacaoInvalidaError(FrotaError):
    pass

class PoliticaNaoAtendidaError(FrotaError):
    pass