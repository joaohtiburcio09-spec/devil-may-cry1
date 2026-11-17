from config import get_connection
from models.missao import Missao

class MissaoDAO:
    def listar_todas(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM missoes")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Missao(r["titulo"], r["recompensa"], r["status"], r["cacador_id"], r["id"]) for r in rows]

    def inserir(self, missao: Missao):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO missoes (titulo, recompensa, status, cacador_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (missao.titulo, missao.recompensa, missao.status, missao.cacador_id))
        conn.commit()
        missao.id = cursor.lastrowid
        cursor.close()
        conn.close()
        return missao

    def concluir(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE missoes SET status = 'Concluída' WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def deletar(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM missoes WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()