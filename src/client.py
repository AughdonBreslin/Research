import json

import requests

# Open config.json
with open('config.json') as config_file:
    config = json.load(config_file)

# Basic POST request
def api_post(data):
    response = requests.post(f"http://{config['HOST']}:{config['PORT']}/api", json=data)
    return response.json()

# Basic GET request
def api_get():
    response = requests.get(f"http://{config['HOST']}:{config['PORT']}/api")
    return response.json()

# Run the app
if __name__ == '__main__':
    print(api_post({'Hello': 'World'}))
    print(api_get())