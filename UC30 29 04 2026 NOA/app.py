from flask import Flask
app = Flask(__name__)

@app.route("/usuario")
def usuario():
    usuario ={
        "nome": "Artur",
        "email": "arturduv@gmail.com",}
    return "pagina de usuario"
@app.route("/pagina_de_usuario")
def contato():
    nome = "Artur"
    return render_template('contato.html', title= 'pagina inicial', nome = nome)
@app.route("/home")
def home():
    return render_template('contato.html', title='Home', nome='Artur')

@app.route('/dados', defaults={"nome": "Usuário comum",})
@app.route('/dados/<nome>')
def dados(nome):
    return f"Olá, {nome}!"

@app.route('/semestre/<int:x>')
def semestre(x):
    return 'Estamos no Semestre ' + str(x)

@app.route('/pagamento/<float:valor>')
def pagamento(valor):
    return "Você pagou: " + str(valor)

@app.route('/somar', defaults={"n1": 0, "n2": 0})
@app.route('/somar/<int:n1>/<int:n2>')
def somar(n1, n2):
    resultado = n1 + n2
    return render_template('somar.html', n1=n1, n2=n2, resultado=resultado)

@app.route('/arearestrita/<int:id>')
def area_restrita(id):
    if id == 1:
        return "Acesso bloqueado!"
    else:
        return "Acesso liberado!"
    

@app.route("/")
def contato():
    nome = "Artur"
    return render_template('contato.html', title= 'pagina inicial', nome = nome)

@app.route("/home")
def home():
    return render_template

@app.route('/dados', defaults={"nome": "visitante",})
@app.route('/dados/<nome>')
def dados(nome):
    return f"Olá, {nome}!"

if __name__ == "__main__":
    app.run(debug=True)

