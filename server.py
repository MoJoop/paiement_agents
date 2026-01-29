from flask import Flask, jsonify, send_file
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Configuration KoBoToolbox
KOBO_CONFIG = {
    "token": "6d13fb1116415f38d3d24c9a4dc2ae411b60abc8",
    "form_id": "anY9a5oozGNEZW87necXjM",
    "base_url": "https://kf.kobotoolbox.org"
}


@app.route("/")
def index():
    """Sert la page HTML principale"""
    return send_file("index.html")


@app.route("/api/data")
def get_kobo_data():
    """Proxy pour récupérer les données KoBoToolbox"""
    try:
        url = f"{KOBO_CONFIG['base_url']}/api/v2/assets/{KOBO_CONFIG['form_id']}/data.json"

        headers = {
            "Authorization": f"Token {KOBO_CONFIG['token']}"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        return jsonify(data)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("=" * 50)
    print("Serveur démarré sur http://localhost:5000")
    print("Ouvrez cette adresse dans votre navigateur")
    print("=" * 50)
    app.run(debug=True, port=5000)
