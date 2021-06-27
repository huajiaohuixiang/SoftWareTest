from flask import Flask
from controller import api
from flask_cors import CORS


def create_app():
    app = Flask(__name__, static_url_path='')
    CORS(app, resources='/*')
    api.init_app(app)
    return app



app=create_app()
app.run(debug=True)
