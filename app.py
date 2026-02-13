import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
DATABASE = "database.db"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------
# CONEXÃO COM BANCO
# -----------------------------
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# -----------------------------
# CRIAR TABELAS AUTOMATICAMENTE
# -----------------------------
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            nome_arquivo TEXT NOT NULL,
            data TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL,
            data TEXT NOT NULL,
            documento_id INTEGER NOT NULL,
            FOREIGN KEY (documento_id) REFERENCES documentos (id)
        )
    """)

    conn.commit()
    conn.close()

init_db()

# -----------------------------
# ROTA PRINCIPAL
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()

    if request.method == "POST":
        file = request.files["file"]
        titulo = request.form["titulo"]
        descricao = request.form.get("descricao")

        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            conn.execute(
                "INSERT INTO documentos (titulo, descricao, nome_arquivo, data) VALUES (?, ?, ?, ?)",
                (titulo, descricao, file.filename, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            )
            conn.commit()

        conn.close()
        return redirect(url_for("index"))

    documentos = conn.execute("SELECT * FROM documentos").fetchall()

    documentos_com_comentarios = []

    for doc in documentos:
        comentarios = conn.execute(
            "SELECT * FROM comentarios WHERE documento_id = ? ORDER BY id DESC",
            (doc["id"],)
        ).fetchall()

        documentos_com_comentarios.append({
            "id": doc["id"],
            "titulo": doc["titulo"],
            "descricao": doc["descricao"],
            "nome_arquivo": doc["nome_arquivo"],
            "data": doc["data"],
            "comentarios": comentarios
        })

    conn.close()
    return render_template("index.html", documentos=documentos_com_comentarios)

# -----------------------------
# DOWNLOAD
# -----------------------------
@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# -----------------------------
# COMENTÁRIOS
# -----------------------------
@app.route("/comentar/<int:doc_id>", methods=["POST"])
def comentar(doc_id):
    comentario_texto = request.form["comentario"]

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO comentarios (texto, data, documento_id) VALUES (?, ?, ?)",
        (comentario_texto, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), doc_id)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
