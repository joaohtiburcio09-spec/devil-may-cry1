from flask import Blueprint, request, jsonify, render_template
from dao.missao_dao import MissaoDAO
from dao.arma_dao import ArmaDAO
from models.missao import Missao
from models.arma import Arma

missoes_bp = Blueprint("missoes", __name__)
missao_dao = MissaoDAO()
arma_dao = ArmaDAO()

@missoes_bp.route("/favoritos")
def pagina_favoritos():
    return render_template("favoritos.html")

# --- Rotas de Missões ---
@missoes_bp.route("/api/missoes", methods=["GET"])
def api_listar_missoes():
    return jsonify([m.to_dict() for m in missao_dao.listar_todas()])

@missoes_bp.route("/api/missoes", methods=["POST"])
def api_criar_missao():
    dados = request.get_json()
    nova = Missao(
        titulo=dados["titulo"],
        recompensa=dados["recompensa"],
        status=dados.get("status", "Pendente"),
        cacador_id=dados.get("cacador_id") or None
    )
    criada = missao_dao.inserir(nova)
    return jsonify(criada.to_dict()), 201

@missoes_bp.route("/api/missoes/<int:id>/concluir", methods=["PUT"])
def api_concluir_missao(id):
    missao_dao.concluir(id)
    return jsonify({"mensagem": "Missão concluída"})

@missoes_bp.route("/api/missoes/<int:id>", methods=["DELETE"])
def api_deletar_missao(id):
    missao_dao.deletar(id)
    return jsonify({"mensagem": "Missão removida"})

@missoes_bp.route("/api/armas", methods=["GET"])
def api_listar_armas():
    return jsonify([a.to_dict() for a in arma_dao.listar_todas()])

@missoes_bp.route("/api/armas", methods=["POST"])
def api_criar_arma():
    dados = request.get_json()
    nova = Arma(dados["nome"], dados["tipo"], int(dados["dano"]), dados.get("cacador_id") or None)
    criada = arma_dao.inserir(nova)
    return jsonify(criada.to_dict()), 201