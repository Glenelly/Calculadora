import os
import asyncio
from urllib.parse import urlparse
from flask import Flask, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from asgiref.sync import async_to_sync
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do Flask
app = Flask(__name__)
CORS(app)

# Configuração do banco de dados para SQLAlchemy síncrono (se necessário)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configuração do SQLAlchemy assíncrono para Neon
tmpPostgres = urlparse(os.getenv("DATABASE_URL"))
async_engine = create_async_engine(
    f"postgresql+asyncpg://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}{tmpPostgres.path}?sslmode=require",
    echo=True,
)

# Diretórios do frontend
frontend_folder = os.path.join(os.getcwd(), "..", "frontend", "dist")
dist_folder = os.path.join(frontend_folder, "dist")

# Rota principal para o frontend
@app.route("/", defaults={"filename": ""})
@app.route("/<path:filename>")
def index(filename):
    if not filename:
        filename = "index.html"
    return send_from_directory(dist_folder, filename)

# Rota para executar uma consulta assíncrona no Neon
@app.route("/async-query")
def async_query():
    """Rota para executar uma consulta assíncrona."""
    async def fetch_data():
        async with async_engine.connect() as conn:
            result = await conn.execute(text("select 'Hello from Neon!'"))
            return [row[0] for row in result.fetchall()]
    
    # Executa a função assíncrona de forma síncrona usando asgiref
    result = async_to_sync(fetch_data)()
    return jsonify({"message": result})

if __name__ == "__main__":
    app.run(debug=True)
