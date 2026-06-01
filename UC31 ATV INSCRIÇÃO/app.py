from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inscricao():
    mensagem = ""
    sucesso = False

    if request.method == "POST":
        nickname = request.form.get("nickname", "").strip()
        jogo = request.form.get("jogo", "").strip()
        email = request.form.get("email", "").strip()

        if len(nickname) < 4 or not jogo or not email:
            mensagem = "Preencha todos os campos obrigatórios."
            sucesso = False
        else:
            mensagem = "Inscrição realizada com sucesso!"
            sucesso = True

    return render_template("index.html", mensagem=mensagem, sucesso=sucesso)

if __name__ == "__main__":
    app.run(debug=True)
