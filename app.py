import swagger_server

import connexion

from swagger_server import encoder

app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'SentInsta'}, pythonic_params=True)

if __name__ == '__main__':
    app.run(port=8080)