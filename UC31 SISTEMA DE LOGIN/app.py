from flask import Flask, render_template, request, redirect, session, url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'sua_chave123445')

usuarios = {
    "Artur": "senhalegal123445",
    "Admin": "123445"
}

@app.route('/')
def home():
    return render_template("inicio.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None

    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        senha = request.form.get("senha", "")

        if usuario in usuarios and usuarios[usuario] == senha:
            session["usuario"] = usuario
            return redirect(url_for("dashboard"))
        else:
            erro = "Usuário ou senha inválidos."

    return render_template("login.html", erro=erro)

@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        usuario=session.get("usuario")
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/rotalogin")
def rotalogin():
    return """
    <h1>Rota Login</h1>
    <p>Esta é a rota extra solicitada pela atividade.</p>
    <a href='/login'>Ir para Login</a>"""

if __name__ == '__main__':
    app.run(debug=True)