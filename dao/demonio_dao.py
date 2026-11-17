from config import get_connection
from models.demonio import Demonio

class DemonioDAO:
    def listar_todos(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM demonios")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Demonio(r["nome"], r["classe"], r["nivel_ameaca"], r["id"]) for r in rows]

    def inserir(self, demonio: Demonio):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO demonios (nome, classe, nivel_ameaca) VALUES (%s, %s, %s)"
        cursor.execute(sql, (demonio.nome, demonio.classe, demonio.nivel_ameaca))
        conn.commit()
        demonio.id = cursor.lastrowid
        cursor.close()
        conn.close()
        return demonio

    def deletar(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM demonios WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()