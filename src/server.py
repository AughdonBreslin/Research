import json

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Open config.json
with open('config.json') as config_file:
    config = json.load(config_file)

# Basic POST request
@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    if data is None or data == {}:
        return jsonify({'error': 'No data provided.'}), 400
    print(data)
    return jsonify(data), 200

# Basic GET request
@app.route('/api', methods=['GET'])
def api_get():
    return jsonify({'Hello': 'World'}), 200

# Run the app
if __name__ == '__main__':
    app.run(host=config['HOST'], port=config['PORT'], debug=config['DEBUG'])

