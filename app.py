import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

documentos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        file = request.files["file"]
        titulo = request.form["titulo"]
        descricao = request.form.get("descricao")

        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            novo_documento = {
                "id": len(documentos),
                "titulo": titulo,
                "descricao": descricao,
                "nome_arquivo": file.filename,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "comentarios": []
            }

            documentos.append(novo_documento)

        return redirect(url_for("index"))

    return render_template("index.html", documentos=documentos)


@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/comentar/<int:doc_id>", methods=["POST"])
def comentar(doc_id):
    comentario_texto = request.form["comentario"]

    comentario = {
        "texto": comentario_texto,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    documentos[doc_id]["comentarios"].append(comentario)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

