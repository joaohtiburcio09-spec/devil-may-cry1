
class Versiculo:
    def __init__(self, numero, texto):
        self.numero = numero
        self.texto = texto

    def exibir_versiculo(self):
        return f"{self.numero}. {self.texto}"
