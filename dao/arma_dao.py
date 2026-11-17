from config import get_connection
from models.arma import Arma

class ArmaDAO:
    def listar_todas(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM armas")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Arma(r["nome"], r["tipo"], r["dano"], r["cacador_id"], r["id"]) for r in rows]

    def inserir(self, arma: Arma):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO armas (nome, tipo, dano, cacador_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (arma.nome, arma.tipo, arma.dano, arma.cacador_id))
        conn.commit()
        arma.id = cursor.lastrowid
        cursor.close()
        conn.close()
        return arma

    def atualizar(self, arma: Arma):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE armas SET nome = %s, tipo = %s, dano = %s, cacador_id = %s WHERE id = %s"
        cursor.execute(sql, (arma.nome, arma.tipo, arma.dano, arma.cacador_id, arma.id))
        conn.commit()
        cursor.close()
        conn.close()

    def deletar(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM armas WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()