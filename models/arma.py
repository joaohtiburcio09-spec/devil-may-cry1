class Arma:
    def __init__(self, nome, tipo, dano, cacador_id=None, id=None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
        self.cacador_id = cacador_id

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo,
            "dano": self.dano,
            "cacador_id": self.cacador_id
        }