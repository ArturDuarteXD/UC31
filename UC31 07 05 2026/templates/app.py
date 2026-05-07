from flask import Flask, render_template

app = Flask(__name__)

@app.route('/filme/<genero>')
def filme(genero):

    if genero == "Ação":
        dados = {
            "titulo": "Filmes de Ação",
            "imagem": "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
            "descricao": "Esse não está disponível no sistema!"
        }

    elif genero == "Comédia":
        dados = {
            "titulo": "Filmes de Comédia",
            "imagem": "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
            "descricao": "Esse não está disponível no sistema!"
        }

    elif genero == "Terror":
        dados = {
            "titulo": "Filmes de Terror",
            "imagem": "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
            "descricao": "Esse não está disponível no sistema!"
        }

    else:
        dados = {
            "titulo": "Gênero não encontrado!",
            "imagem": "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
            "descricao": "Esse gênero não está disponível no sistema!"
        }

    return render_template("filme.html", dados=dados)

if __name__ == '__main__':
    app.run(debug=True)
    