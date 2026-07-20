from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
ARQUIVO = 'livros.json'

def ler():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        return []
    with open(ARQUIVO, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar(dados):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def validar(f):
    t, a, y, c, q = f.get('titulo',''), f.get('autor',''), f.get('ano',''), f.get('categoria',''), f.get('quantidade','')
    if not all([t, a, y, c, q]):
        return "Todos os campos devem ser preenchidos!"
    if not y.isdigit():
        return "O ano de publicação deve conter apenas números."
    if not q.isdigit() or int(q) <= 0:
        return "A quantidade deve ser um número inteiro maior que zero."
    return None

@app.route('/', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        erro = validar(request.form)
        if erro:
            return render_template('cadastro.html', erro_mensagem=erro)
        
        livros = ler()
        livros.append({
            'titulo': request.form['titulo'].strip(),
            'autor': request.form['autor'].strip(),
            'ano': int(request.form['ano']),
            'categoria': request.form['categoria'].strip(),
            'quantidade': int(request.form['quantidade'])
        })
        salvar(livros)
        return redirect(url_for('listar'))
    return render_template('cadastro.html', erro_mensagem=None)

@app.route('/livros')
def listar():
    return render_template('livros.html', livros_cadastrados=ler())

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    resultado, msg = None, None
    if request.method == 'POST':
        busca = request.form.get('busca', '').strip().lower()
        for livro in ler():
            if busca in livro['titulo'].lower():
                resultado = livro
                break
        if not resultado:
            msg = "Livro não encontrado."
    return render_template('buscar.html', livro_encontrado=resultado, mensagem_erro=msg)

@app.route('/editar/<int:indice>', methods=['GET', 'POST'])
def editar(indice):
    livros = ler()
    if indice < 0 or indice >= len(livros):
        return redirect(url_for('listar'))

    if request.method == 'POST':
        erro = validar(request.form)
        if erro:
            return render_template('editar.html', livro=livros[indice], id_livro=indice, erro_mensagem=erro)
        
        livros[indice] = {
            'titulo': request.form['titulo'].strip(),
            'autor': request.form['author'].strip() if 'author' in request.form else request.form['autor'].strip(),
            'ano': int(request.form['ano']),
            'categoria': request.form['categoria'].strip(),
            'quantidade': int(request.form['quantidade'])
        }
        salvar(livros)
        return redirect(url_for('listar'))
    return render_template('editar.html', livro=livros[indice], id_livro=indice, erro_mensagem=None)

@app.route('/excluir/<int:indice>')
def excluir(indice):
    livros = ler()
    if 0 <= indice < len(livros):
        livros.pop(indice)
        salvar(livros)
    return redirect(url_for('listar'))

if __name__ == '__main__':
    app.run(debug=True)