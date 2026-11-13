
from config import conectar
from models.demonio import Demonio


class DemonioDAO:

    def cadastrar(self, demonio):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO demonios (nome, categoria, nivel_perigo)
        VALUES (%s, %s, %s)
        """

        valores = (
            demonio.nome,
            demonio.categoria,
            demonio.nivel_perigo
        )

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

    def consultar_todos(self):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT * FROM demonios")
        resultados = cursor.fetchall()

        cursor.close()
        conexao.close()

        return resultados
