
import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="devil_may_cry"
    )

    return conexao
