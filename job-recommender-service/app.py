from flask import Flask
from flasgger import Swagger
from api.route.search import search_api
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:3000"])
     ## Initialize Config
    app.config.from_pyfile('config.py')
    app.register_blueprint(search_api, url_prefix='/api')

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
