from config import get_connection
from models.cacador import Cacador

class CacadorDAO:
    def listar_todos(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cacadores")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Cacador(r["nome"], r["especialidade"], r["rank_estilo"], r["id"]) for r in rows]

    def inserir(self, cacador: Cacador):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO cacadores (nome, especialidade, rank_estilo) VALUES (%s, %s, %s)"
        cursor.execute(sql, (cacador.nome, cacador.especialidade, cacador.rank_estilo))
        conn.commit()
        cacador.id = cursor.lastrowid
        cursor.close()
        conn.close()
        return cacador

    def deletar(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cacadores WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()