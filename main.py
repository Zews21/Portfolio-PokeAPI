from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", pokemon=None)


@app.route('/pokemon', methods=['POST'])
def get_pokemon():
    pokemon_name = request.form.get('pokemon_name').lower()

    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')

    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_image_url = pokemon_data['sprites']['front_default']
        return render_template("index.html", pokemon=pokemon_data, image_url=pokemon_image_url)
    else:
        error_message = "Pokémon not found. Please try another name."
        return render_template("index.html", pokemon=None, error=error_message)


if __name__ == '__main__':
    app.run(debug=True)
