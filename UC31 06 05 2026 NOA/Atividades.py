from flask import flask

app = Flask(__name__)

@app.route('/arearestrita/<int:id>')
def area_restrita(id):
    if id == 1:
        return "Cadeado fechado!"
    if id == 2:
        return "Cadeado aberto!"
    else:
        return "ID inválido!"

@app.route("/operacao/<tipo>/<float:op1>/<float:op2>")
def operacao(tipo, op1, op2):
    if tipo == "sum":
        resultado = op1 + op2
    elif tipo == "sub":
        resultado = op1 - op2
    elif tipo == "mult":
        resultado = op1 * op2
    elif tipo == "div":
        if op2 == 0:
            return "Erro: divisão por zero!"
        resultado = op1 / op2
    else:
        return "Tipo inválido! Use: sum, sub, mult ou div."

    return f"Resultado: {resultado}"


if __name__ == "__main__":
    app.run(debug=True)
