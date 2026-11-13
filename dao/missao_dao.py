
from config import conectar
from models.missao import Missao


class MissaoDAO:

    def cadastrar(self, missao):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO missoes
        (titulo, descricao, dificuldade, status, cacador_id, demonio_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (
            missao.titulo,
            missao.descricao,
            missao.dificuldade,
            missao.status,
            missao.cacador_id,
            missao.demonio_id
        )

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

    def consultar_todos(self):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT * FROM missoes")
        resultados = cursor.fetchall()

        cursor.close()
        conexao.close()

        return resultados
