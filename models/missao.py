class Missao:
    def __init__(self, titulo, recompensa, status="Pendente", cacador_id=None, id=None):
        self.id = id
        self.titulo = titulo
        self.recompensa = float(recompensa)
        self.status = status
        self.cacador_id = cacador_id

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "recompensa": self.recompensa,
            "status": self.status,
            "cacador_id": self.cacador_id
        }