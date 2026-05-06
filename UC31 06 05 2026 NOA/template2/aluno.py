from flask import Flask, render_template

app = Flask(__name__)

# Rota /login
@app.route('/login')
def login():
    return render_template('login.html')

# Rota /alunos
@app.route('/alunos')
def alunos():
    lista_alunos = [
        {"nome": "Alic", "matricula": "12345678"},
        {"nome": "Bruno", "matricula": "987654321"},
        {"nome": "Clara", "matricula": "45678912"},
        {"nome": "Marilson", "matricula": "74125896"},
        {"nome": "Valéria", "matricula": "85236974"}
    ]
    
    return render_template('alunos.html', alunos=lista_alunos)

if __name__ == '__main__':
    app.run(debug=True)