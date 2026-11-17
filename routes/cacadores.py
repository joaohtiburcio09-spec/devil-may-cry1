from flask import Blueprint, request, jsonify, render_template
from dao.cacador_dao import CacadorDAO
from models.cacador import Cacador

cacadores_bp = Blueprint("cacadores", __name__)
dao = CacadorDAO()

@cacadores_bp.route("/cacadores")
def pagina_cacadores():
    return render_template("cacadores.html")

@cacadores_bp.route("/api/cacadores", methods=["GET"])
def api_listar_cacadores():
    lista = dao.listar_todos()
    return jsonify([c.to_dict() for c in lista])

@cacadores_bp.route("/api/cacadores", methods=["POST"])
def api_criar_cacador():
    dados = request.get_json()
    novo = Cacador(
        nome=dados["nome"],
        especialidade=dados["especialidade"],
        rank_estilo=dados.get("rank_estilo", "SSS")
    )
    criado = dao.inserir(novo)
    return jsonify(criado.to_dict()), 201

@cacadores_bp.route("/api/cacadores/<int:id>", methods=["DELETE"])
def api_deletar_cacador(id):
    dao.deletar(id)
    return jsonify({"mensagem": "Caçador removido com sucesso"})