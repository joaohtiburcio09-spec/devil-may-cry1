
class Missao:
    def __init__(self, titulo, descricao, dificuldade,
                 cacador_id, demonio_id, status="Pendente", id=None):

        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.dificuldade = dificuldade
        self.status = status
        self.cacador_id = cacador_id
        self.demonio_id = demonio_id
