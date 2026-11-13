
from flask import Flask, request, jsonify
from config import conectar
from models.cacador import Cacador
from dao.cacador_dao import CacadorDAO

app = Flask(__name__)

dao = CacadorDAO()


# Página inicial
@app.route("/")
def inicio():
    return "Devil May Cry - Devil Hunter Agency"


# Cadastrar caçador
@app.route("/cacadores", methods=["POST"])
def cadastrar_cacador():
    dados = request.get_json()

    if not dados or not all(
        campo in dados for campo in ("nome", "idade", "rank")
    ):
        return jsonify({"erro": "Informe nome, idade e rank"}), 400

    try:
        idade = int(dados["idade"])

        if idade <= 0:
            return jsonify({"erro": "A idade deve ser maior que zero"}), 400

        cacador = Cacador(
            dados["nome"],
            idade,
            dados["rank"]
        )

        dao.cadastrar(cacador)

        return jsonify({"mensagem": "Caçador cadastrado com sucesso!"}), 201

    except (ValueError, TypeError):
        return jsonify({"erro": "Idade inválida"}), 400


# Consultar todos os caçadores
@app.route("/cacadores", methods=["GET"])
def consultar_cacadores():
    cacadores = dao.consultar_todos()
    return jsonify(cacadores)


# Consultar caçador pelo ID
@app.route("/cacadores/<int:id>", methods=["GET"])
def consultar_cacador(id):
    cacador = dao.consultar_por_id(id)

    if cacador:
        return jsonify(cacador)

    return jsonify({"erro": "Caçador não encontrado"}), 404


# Editar caçador
@app.route("/cacadores/<int:id>", methods=["PUT"])
def editar_cacador(id):
    dados = request.get_json()

    if not dados or not all(
        campo in dados for campo in ("nome", "idade", "rank")
    ):
        return jsonify({"erro": "Informe nome, idade e rank"}), 400

    try:
        idade = int(dados["idade"])

        if idade <= 0:
            return jsonify({"erro": "A idade deve ser maior que zero"}), 400

        cacador = Cacador(
            dados["nome"],
            idade,
            dados["rank"]
        )

        if dao.editar(id, cacador):
            return jsonify({"mensagem": "Caçador atualizado!"})

        return jsonify({"erro": "Caçador não encontrado"}), 404

    except (ValueError, TypeError):
        return jsonify({"erro": "Idade inválida"}), 400


# Excluir caçador
@app.route("/cacadores/<int:id>", methods=["DELETE"])
def excluir_cacador(id):
    if dao.excluir(id):
        return jsonify({"mensagem": "Caçador excluído!"})

    return jsonify({"erro": "Caçador não encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)
    
from models.demonio import Demonio
from dao.demonio_dao import DemonioDAO

from models.missao import Missao
from dao.missao_dao import MissaoDAO