from flask import Flask, render_template
from routes.cacadores import cacadores_bp
from routes.demonios import demonios_bp
from routes.missoes import missoes_bp

app = Flask(__name__)

# Registro das rotas (Blueprints)
app.register_blueprint(cacadores_bp)
app.register_blueprint(demonios_bp)
app.register_blueprint(missoes_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)