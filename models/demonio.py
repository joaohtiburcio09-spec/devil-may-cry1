class Demonio:
    def __init__(self, nome, classe, nivel_ameaca, id=None):
        self.id = id
        self.nome = nome
        self.classe = classe
        self.nivel_ameaca = nivel_ameaca

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "classe": self.classe,
            "nivel_ameaca": self.nivel_ameaca
        }