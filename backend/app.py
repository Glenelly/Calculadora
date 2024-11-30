from flask import Flask, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

app = Flask(__name__)
CORS(app)

DATABASE_URL = os.getenv("DATABASE_URL")

print("Conectando ao banco de dados:", DATABASE_URL)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

frontend_folder = os.path.join(os.getcwd(), "..", "frontend", "dist")
dist_folder = os.path.join(frontend_folder, "dist")

@app.route("/", defaults={"filename": ""})
@app.route("/<path:filename>")
def index(filename):
    if not filename:
        filename = "index.html"
    return send_from_directory(dist_folder, filename)

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    
    result = db.session.execute("SELECT * FROM usuarios")
    users = result.fetchall()
    return jsonify([dict(user) for user in users])

if __name__ == '__main__':
    app.run(debug=True)

