from flask import Blueprint, request, jsonify, render_template
from dao.demonio_dao import DemonioDAO
from models.demonio import Demonio

demonios_bp = Blueprint("demonios", __name__)
dao = DemonioDAO()

@demonios_bp.route("/demonios")
def pagina_demonios():
    return render_template("demonios.html")

@demonios_bp.route("/api/demonios", methods=["GET"])
def api_listar_demonios():
    return jsonify([d.to_dict() for d in dao.listar_todos()])

@demonios_bp.route("/api/demonios", methods=["POST"])
def api_criar_demonio():
    dados = request.get_json()
    novo = Demonio(dados["nome"], dados["classe"], int(dados["nivel_ameaca"]))
    criado = dao.inserir(novo)
    return jsonify(criado.to_dict()), 201

@demonios_bp.route("/api/demonios/<int:id>", methods=["DELETE"])
def api_deletar_demonio(id):
    dao.deletar(id)
    return jsonify({"mensagem": "Demônio removido"})