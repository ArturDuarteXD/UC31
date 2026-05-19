from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    lanches = [
        'X-Burguer',
        'X-Bacon',
        'X-Tudo'
    ]

    return render_template('cardapio.html', lanches=lanches)

@app.route('/pedidos')
def pedidos():
    pedidos = [
        'Pedido 1',
        'Pedido 2',
        'Pedido 3'
    ]

    return render_template('pedidos.html', pedidos=pedidos)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/cliente/<nome>')
def cliente(nome):
    return render_template('cliente.html', nome=nome)

@app.route('/lanche/<nome>')
def lanche(nome):
    return render_template('lanche.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)