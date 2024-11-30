from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate  # Importação do Flask-Migrate
import os

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Configuração do Flask-Migrate
migrate = Migrate(app, db)  # Inicialização do Migrate com a aplicação e o banco de dados

frontend_folder = os.path.join(os.getcwd(), "..", "frontend", "dist")
dist_folder = os.path.join(frontend_folder, "dist")

@app.route("/", defaults={"filename": ""})
@app.route("/<path:filename>")
def index(filename):
    if not filename:
        filename = "index.html"
    return send_from_directory(dist_folder, filename)
