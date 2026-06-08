from flask import {
    Flask,
    Render_Tempalate,
    Request,
    Make_response
    Redirect,
    url_for,
}

app = Flask(__name__)

@app.route('/')
def inicio():
    tema = request.cookies.get('tema', 'Claro')
    return render_template(
        'inicio.html'
        tema = tema
    )

@app.route('/tema/<escolha>')
def trocar_tema(escolha):
    
    if escolha not in ['claro', 'escuro']
        escolha = 'claro'

    resposta = make_response(
        redirect(url_for('Início'))
    )

    resposta.set_cookie(
        'tema',
        escolha,
        max_age=60*60*24*30
    )

    return resposta
