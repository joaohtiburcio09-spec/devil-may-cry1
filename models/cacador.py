class Cacador:
    def __init__(self, nome, especialidade, rank_estilo="SSS", id=None):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade
        self.rank_estilo = rank_estilo

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "especialidade": self.especialidade,
            "rank_estilo": self.rank_estilo
        }