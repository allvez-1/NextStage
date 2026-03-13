from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Conexão com banco de dados
def conectar():
    return sqlite3.connect("database.db")


# Criar tabelas
def criar_banco():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vagas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        empresa TEXT,
        titulo TEXT,
        descricao TEXT,
        requisitos TEXT,
        prazo TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidaturas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        curriculo TEXT,
        vaga_id INTEGER
    )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastrar_vaga", methods=["GET", "POST"])
def cadastrar_vaga():
    if request.method == "POST":

        empresa = request.form["empresa"]
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        requisitos = request.form["requisitos"]
        prazo = request.form["prazo"]

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO vagas (empresa,titulo,descricao,requisitos,prazo)
        VALUES (?,?,?,?,?)
        """, (empresa,titulo,descricao,requisitos,prazo))

        conn.commit()
        conn.close()

        return redirect("/vagas")

    return render_template("cadastrar_vaga.html")


@app.route("/vagas")
def vagas():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM vagas")
    vagas = cursor.fetchall()

    conn.close()

    return render_template("vagas.html", vagas=vagas)


@app.route("/candidatar/<int:vaga_id>", methods=["GET","POST"])
def candidatar(vaga_id):

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        curriculo = request.form["curriculo"]

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO candidaturas (nome,email,curriculo,vaga_id)
        VALUES (?,?,?,?)
        """,(nome,email,curriculo,vaga_id))

        conn.commit()
        conn.close()

        return "Candidatura enviada com sucesso!"

    return render_template("candidatura.html", vaga_id=vaga_id)


if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)
    import os

UPLOAD_FOLDER = "uploads/curriculos"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
file = request.files["curriculo"]

if file:
    caminho = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(caminho)
    @app.route("/buscar")
    def buscar():

    termo = request.args.get("q")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM vagas
    WHERE titulo LIKE ?
    """, ('%'+termo+'%',))

    vagas = cursor.fetchall()

    return render_template("vagas.html", vagas=vagas)