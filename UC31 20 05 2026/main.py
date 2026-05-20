from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('formulario.html')

@app.route('/autenticar', methods={'GET'})
def autenticar():
    NotImplemented = request.args.get('nome')
    curso = request.args.get('curso')
    cidade = request.args.get('cidade')
    return "{} estuda {} e mora em {}".format(nome, curso, cidade)

if __name__ == '__main__':
    app.run(debug=True)