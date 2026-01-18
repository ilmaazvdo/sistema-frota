class Pessoa:  
    """Classe base para aplicar Herança Simples conforme requisito."""
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

class Motorista(Pessoa):
    """Gerencia dados do motorista e validações de alocação."""
    def __init__(self, nome, cpf, categoria_cnh):
        # Chama o construtor da classe pai (Pessoa)
        super().__init__(nome, cpf)
        self._categoria_cnh = categoria_cnh.upper()

    @property
    def categoria_cnh(self):
        return self._categoria_cnh

    # --- MÉTODOS ESPECIAIS (Requisito de POO) ---
    def __str__(self):
        """Representação amigável para o menu do Gyan."""
        return f"Motorista: {self._nome} [CNH: {self._categoria_cnh}]"

    def __eq__(self, outro):
        """Compara se é o mesmo motorista pelo CPF (evita duplicados)."""
        if not isinstance(outro, Motorista):
            return False
        return self._cpf == outro.cpf

    def __repr__(self):
        """Representação técnica para o repositório do Nataniel."""
        return f"Motorista(nome='{self._nome}', cnh='{self._categoria_cnh}')"

    # --- REGRA DE NEGÓCIO ---
    def pode_dirigir(self, veiculo):
        """
        Verifica se o motorista tem a CNH correta e se o veículo está ativo.
        Esta lógica será usada pelo Nataniel na camada de serviços.
        """
        if veiculo.status == "MANUTENCAO":
            return False, "BLOQUEADO: Veículo em manutenção."

        # Mapeamento básico de categorias (pode ser expandido via settings.json)
        cnh_requerida = getattr(veiculo, 'cnh_requerida', 'B') # Padrão B se não definido
        
        if self._categoria_cnh == cnh_requerida or self._categoria_cnh in ['D', 'E']:
            return True, "AUTORIZADO: CNH compatível."
        
        return False, f"NEGADO: CNH {self._categoria_cnh} incompatível com {veiculo.tipo}."
