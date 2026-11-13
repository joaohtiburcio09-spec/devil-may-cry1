
from config import conectar
from models.cacador import Cacador


class CacadorDAO:

    # Cadastrar um novo caçador
    def cadastrar(self, cacador):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO cacadores (nome, idade, rank)
        VALUES (%s, %s, %s)
        """

        valores = (cacador.nome, cacador.idade, cacador.rank)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        return True

    # Consultar todos os caçadores
    def consultar_todos(self):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT * FROM cacadores")
        resultados = cursor.fetchall()

        cursor.close()
        conexao.close()

        return resultados

    # Consultar um caçador pelo ID
    def consultar_por_id(self, id):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM cacadores WHERE id = %s",
            (id,)
        )

        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()

        return resultado

    # Editar um caçador
    def editar(self, id, cacador):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        UPDATE cacadores
        SET nome = %s, idade = %s, rank = %s
        WHERE id = %s
        """

        valores = (cacador.nome, cacador.idade, cacador.rank, id)

        cursor.execute(sql, valores)
        conexao.commit()

        alterados = cursor.rowcount

        cursor.close()
        conexao.close()

        return alterados > 0

    # Excluir um caçador
    def excluir(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM cacadores WHERE id = %s",
            (id,)
        )

        conexao.commit()

        excluidos = cursor.rowcount

        cursor.close()
        conexao.close()

        return excluidos > 0
