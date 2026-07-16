from flask import flask, render_template
import json

app = Flask(__nome__)

@app.route("/")
def produtos()

    with open("produtos.json", "r", enconding="utf-8") as arquivo:
        lista_produtos = json.load(arquivo)

    return render_template ("produtos.html", produtos=lista_produtos)

if __nome__ == "__main__":
    app.run(debug=True)