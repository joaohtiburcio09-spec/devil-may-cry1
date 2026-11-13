
class Demonio:
    def __init__(self, nome, categoria, nivel_perigo, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.nivel_perigo = nivel_perigo

    def exibir_informacoes(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "categoria": self.categoria,
            "nivel_perigo": self.nivel_perigo
        }
