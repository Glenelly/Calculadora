from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate  # Importação do Flask-Migrate
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# Usar a variável de ambiente para configurar a URL do banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("postgresql://neondb_owner:mK5ErcHOtuv2@ep-dark-king-a54fcoql.us-east-2.aws.neon.tech/neondb?sslmode=require")
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
